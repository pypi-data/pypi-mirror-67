from logging import getLogger
from itertools import takewhile
from functools import partial

from zope.component.hooks import getSite

from DateTime import DateTime

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage

from emrt.necd.content.roles.localrolesubscriber import grant_local_roles

import openpyxl


LOG = getLogger('emrt.necd.content.carryover')


def _read_col(row, nr):
    val = row[nr].value
    return val.strip() if val else val


def _clear_local_roles(obj):
    obj.__ac_local_roles__ = None


def clear_and_grant_roles(obj):
    """ Clear any local roles already granted and grant just those
        that make sense in the current review folder context.

        [refs #105604] This makes sure that users that were granted
        local roles on the old observation will not continue to
        have them (e.g. CounterPart).
    """
    _clear_local_roles(obj)
    grant_local_roles(obj)


def _copy_obj(target, ob, new_id=None):
    orig_ob = ob
    ob_id = new_id or orig_ob.getId()
    ob = ob._getCopy(target)
    ob._setId(ob_id)
    target._setObject(ob_id, ob)
    return target[ob_id]


def _copy_and_flag(context, obj, new_id=None):
    _, _, year, index = (new_id or obj.getId()).split('-')
    ob = _copy_obj(context, obj, new_id=new_id)
    ob.carryover_from = year
    ob.review_year = int(year)

    LOG.info(
        'Copied %s -> %s',
        obj.absolute_url(1),
        ob.absolute_url(1),
    )

    return ob


def _obj_from_url(context, site_url, url):
    traversable = str(url.split(site_url)[-1][1:])
    return context.unrestrictedTraverse(traversable)


def replace_conclusion_text(obj, text):
    conclusion = obj.get_conclusion()
    if text and conclusion:
        conclusion.text = text


def prepend_qa(target, source):
    source_qa = source.get_question()
    target_qa = target.get_question()

    if source_qa and target_qa:
        for comment in source_qa.values():
            _copy_obj(target_qa, comment)

        ordering = target_qa.getOrdering()
        ordering.orderObjects(key='creation_date')

    elif source_qa and not target_qa:
        _copy_obj(target, source_qa)


def add_to_wh(wf, obj, action, state, actor):
    wh = obj.workflow_history
    wf_id = wf.getId()
    wh[wf_id] = wh[wf_id] + ({
        'comments': 'Carryover force state',
        'actor': actor,
        'time': DateTime(),
        'action': action,
        'review_state': state,
    }, )
    wf.updateRoleMappingsFor(obj)


def reopen_with_qa(wf, wf_q, wf_c, obj, actor):
    add_to_wh(wf, obj, 'reopen-qa-chat', 'pending', actor)
    question = obj.get_question()
    if question:
        add_to_wh(wf_q, question, 'reopen', 'draft', actor)

    conclusion = obj.get_conclusion()
    if conclusion:
        add_to_wh(wf_c, conclusion, 'redraft', 'draft', actor)


def copy_direct(context, catalog, wf, wf_q, wf_c, obj_from_url, row):
    source = _read_col(row, 0)
    conclusion_text = _read_col(row, 1)
    actor = _read_col(row, 2)

    obj = obj_from_url(source)
    ob = _copy_and_flag(context, obj)

    replace_conclusion_text(ob, conclusion_text)
    clear_and_grant_roles(ob)
    reopen_with_qa(wf, wf_q, wf_c, ob, actor)

    catalog.catalog_object(ob)


def copy_complex(context, catalog, wf, wf_q, wf_c, obj_from_url, row):
    source = _read_col(row, 0)
    older_source = _read_col(row, 1)
    conclusion_text = _read_col(row, 2)
    actor = _read_col(row, 3)

    obj = obj_from_url(source)
    older_obj = obj_from_url(older_source)

    ob = _copy_and_flag(context, obj, older_obj.getId())

    replace_conclusion_text(ob, conclusion_text)
    prepend_qa(ob, older_obj)
    clear_and_grant_roles(ob)
    reopen_with_qa(wf, wf_q, wf_c, ob, actor)

    catalog.catalog_object(ob)


class CarryOverView(BrowserView):

    index = ViewPageTemplateFile('templates/carryover.pt')

    def __call__(self):
        return self.index()

    def start(self, action, xls):
        portal = getSite()
        wb = openpyxl.load_workbook(xls, read_only=True, data_only=True)
        sheet = wb.worksheets[0]


        sheet_rows = sheet.rows
        next(sheet_rows)  # skip first row (header)
        # extract rows with values
        valid_rows = tuple(takewhile(
            lambda row: any(c.value for c in row), sheet_rows))

        context = self.context
        site_url = portal.absolute_url()
        obj_from_url = partial(_obj_from_url, context, site_url)
        catalog = getToolByName(portal, 'portal_catalog')
        wft = getToolByName(portal, 'portal_workflow')

        wf_obs = wft.getWorkflowById(wft.getChainFor('Observation')[0])
        wf_question = wft.getWorkflowById(wft.getChainFor('Question')[0])
        wf_conclusion = wft.getWorkflowById(wft.getChainFor('Conclusions')[0])

        actions = dict(direct=copy_direct, complex=copy_complex)
        copy_func = partial(
            actions[action],
            context, catalog,
            wf_obs, wf_question, wf_conclusion,
            obj_from_url
        )

        for row in valid_rows:
            copy_func(row)

        if len(valid_rows) > 0:
            (IStatusMessage(self.request)
                .add('Carryover successfull!', type='info'))
        else:
            (IStatusMessage(self.request)
                .add('No data provided!', type='warn'))
        self.request.RESPONSE.redirect(context.absolute_url())
