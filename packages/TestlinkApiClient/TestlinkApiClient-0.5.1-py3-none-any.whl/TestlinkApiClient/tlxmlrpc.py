#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Will v.stone@163.com

from xmlrpc.client import ServerProxy
from xml.dom.minidom import parse


class TestlinkClient(object):
    def __init__(self, url: str, user: str, dev_key: str, tree=False):
        self.url = url + '/lib/api/xmlrpc/v1/xmlrpc.php'
        self.user = user
        self.dev_key = {
            'devKey': dev_key
        }
        self.client = ServerProxy(self.url).tl
        tl_about = self.client.about()
        print(tl_about)
        print(self.client.ping())
        dev_key_valid = self.client.checkDevKey(self.dev_key)
        assert dev_key_valid is True, dev_key_valid[0].get('message')
        user_valid = self.client.doesUserExist({'devKey': dev_key, 'user': user})
        assert user_valid is True, user_valid[0].get('message')
        self.step_template = {
            'step_number': '1',
            'actions': 'step#1',
            'expected_results': 'result#1',
            'execution_type': '1'  # Manual
        }
        self.tree = tree

    @staticmethod
    def _check_results(rsp_results):
        if isinstance(rsp_results, list) \
                and len(rsp_results) == 1 \
                and isinstance(rsp_results[0], dict) \
                and rsp_results[0].get('code'):
            raise Exception(rsp_results[0])

    def _tree(self, content, root: str = '.'):
        if self.tree is False:
            return True
        if root == '':
            root = '.'
        if content is None:
            _tree_str = root
        elif len(content) == 0:
            _tree_str = root
        elif len(content) == 1:
            content = list(content)
            _tree_str = '%s\n└── %s' % (root, content[0])
        else:
            _tree_str = root
            content = list(content)
            for _str in content[:-1]:
                _tree_str = '\n'.join([
                    _tree_str,
                    '├── %s' % _str
                ])
            _tree_str = _tree_str + '\n└── %s' % content[-1]
        print(_tree_str)
        return True

    def _get_issue_tracker(self, **kwargs):
        """
        tl.getIssueTrackerSystem
        :param kwargs: itsname
        :return:
        """
        itsname = kwargs.get('itsname')
        param = self.dev_key.copy()
        if itsname:
            param['itsname'] = itsname
        else:
            raise KeyError('itsname is required')
        results = self.client.getIssueTrackerSystem(param)
        self._check_results(results)
        return results

    def _create_project(self, **kwargs):
        """
        tl.createTestProject
        :param kwargs: project_name, prefix
        :return:
        """
        project_name = kwargs.get('project_name')
        prefix = kwargs.get('prefix')
        param = self.dev_key.copy()
        if project_name:
            param['testprojectname'] = project_name
        else:
            raise KeyError('project_id is required')
        param['testcaseprefix'] = prefix if prefix else project_name
        results = self.client.createTestProject(param)
        self._check_results(results)
        return results

    def _get_projects(self):
        """
        tl.getProjects
        :return:
        """
        param = self.dev_key.copy()
        results = self.client.getProjects(param)
        self._check_results(results)
        return results

    def _get_project_by_name(self, **kwargs):
        """
        tl.getTestProjectByName
        :param kwargs: project_name
        :return:
        """
        project_name = kwargs.get('project_name')
        param = self.dev_key.copy()
        if project_name:
            param['testprojectname'] = project_name
        else:
            raise KeyError('project_name is required')
        results = self.client.getTestProjectByName(param)
        self._check_results(results)
        return results

    def _get_project_name(self, **kwargs):
        """
        Gte project name by ID
        :param kwargs: project_id
        :return:
        """
        project_id = kwargs.get('project_id')
        if not project_id:
            raise KeyError('project_id is required')
        for project in self._get_projects():
            if project.get('id') == project_id:
                return project.get('name')
        return None

    def _get_project_id(self, **kwargs):
        """
        Get project ID by name
        :param kwargs: project_name
        :return:
        """
        project_name = kwargs.get('project_name')
        if project_name:
            return self._get_project_by_name(project_name=project_name).get('id')
        else:
            raise KeyError('project_name is required')

    def _get_project_prefix(self, **kwargs):
        """
        Get project prefix by project name
        :param kwargs: project_id, project_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        if project_id:
            project_name = self._get_project_name(project_id=project_id)
        elif project_name:
            pass
        else:
            raise KeyError('project_id or project_name is required')
        return self._get_project_by_name(project_name=project_name).get('prefix')

    def _delete_project(self, **kwargs):
        """
        tl.deleteTestProject
        :param kwargs:
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        param = self.dev_key.copy()
        if project_id:
            param['testprojectid'] = project_id
        elif project_name:
            param['testprojectid'] = self._get_project_id(project_name=project_name)
        else:
            raise KeyError('project_id or project_name is required')
        results = self.client.deleteTestProject(param)
        self._check_results(results)
        return results

    def _get_project_test_plans(self, **kwargs):
        """
        tl.getProjectTestPlans
        :param kwargs: project_id, project_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        param = self.dev_key.copy()
        if project_id:
            param['testprojectid'] = project_id
        elif project_name:
            param['testprojectid'] = self._get_project_id(project_name=project_name)
        else:
            raise KeyError('project_id or project_name is required')
        results = self.client.getProjectTestPlans(param)
        self._check_results(results)
        return results

    def _get_requirements(self, **kwargs):
        """
        tl.getRequirements
        :param kwargs: project_id, project_name, plan_id, plan_name, platform_id, platform_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        plan_id = kwargs.get('plan_id')
        plan_name = kwargs.get('plan_name')
        platform_id = kwargs.get('platform_id')
        platform_name = kwargs.get('platform_name')
        param = self.dev_key.copy()
        if project_id:
            param['testprojectid'] = project_id
        elif project_name:
            param['testprojectid'] = self._get_project_id(project_name=project_name)
        else:
            raise KeyError('project_id or project_name is required')
        if plan_id:
            param['testplanid'] = plan_id
        elif plan_name:
            param['testplanid'] = self._get_test_plan_id(
                project_name=project_name, project_id=project_id,
                plan_name=plan_name
            )
        if platform_id:
            param['platformid'] = platform_id
        elif platform_name:
            param['platformname'] = platform_name
        results = self.client.getRequirements(param)
        self._check_results(results)
        return results

    def _get_requirement_coverage(self, **kwargs):
        """

        :param kwargs: project_id, project_name, requirement_doc_id
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        requirement_doc_id = kwargs.get('requirement_doc_id')
        param = self.dev_key.copy()
        if project_id or project_name:
            param['testprojectid'] = project_id if project_id else self._get_project_id(project_name=project_name)
        else:
            raise KeyError('project_id or project_name is required')
        if requirement_doc_id:
            param['requirementdocid'] = requirement_doc_id
        results = self.client.getReqCoverage(param)
        self._check_results(results)
        return results

    def _get_plan_by_name(self, **kwargs):
        """
        tl.getTestPlanByName
        :param kwargs: project_id, project_name, plan_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        plan_name = kwargs.get('plan_name')
        param = self.dev_key.copy()
        if project_id or project_name:
            param['testprojectname'] = project_name if project_name else self._get_project_name(project_id=project_id)
        else:
            raise KeyError('project_id or project_name is required')
        if plan_name:
            param['testplanname'] = plan_name
        else:
            raise KeyError('plan_name is required')
        results = self.client.getTestPlanByName(param)
        self._check_results(results)
        return results

    def _get_test_plan_id(self, **kwargs):
        """
        Get test plan id by name
        :param kwargs: project_id, project_name, plan_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        plan_name = kwargs.get('plan_name')
        if plan_name:
            if project_name or project_id:
                results = self._get_plan_by_name(project_name=project_name, project_id=project_id, plan_name=plan_name)
            else:
                raise KeyError('project_id or project_name is required')
        else:
            raise KeyError('plan_name is required')
        try:
            return results[0].get('id')
        except Exception:
            raise ValueError('No test plan: %s in project: %s' % (plan_name, project_name))

    def _get_builds_for_plan(self, **kwargs):
        """
        tl.getBuildsForTestPlan
        :param kwargs: project_name, project_id, plan_id, plan_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        plan_id = kwargs.get('plan_id')
        plan_name = kwargs.get('plan_name')
        param = self.dev_key.copy()
        if plan_id:
            param['testplanid'] = plan_id
        elif plan_name:
            if project_id or project_name:
                param['testplanid'] = self._get_test_plan_id(project_name=project_name, project_id=project_id,
                                                             plan_name=plan_name)
            else:
                raise KeyError('project_id or project_name is required')
        else:
            raise KeyError('plan_id or plan_name is required')

        results = self.client.getBuildsForTestPlan(param)
        self._check_results(results)
        return results

    def _get_platforms_for_plan(self, **kwargs):
        """
        tl.getTestPlanPlatforms
        :param kwargs: project_name, project_id, plan_id, plan_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        plan_id = kwargs.get('plan_id')
        plan_name = kwargs.get('plan_name')
        param = self.dev_key.copy()
        if plan_id:
            param['testplanid'] = plan_id
        elif plan_name:
            if project_id or project_name:
                param['testplanid'] = self._get_test_plan_id(project_name=project_name, project_id=project_id,
                                                             plan_name=plan_name)
            else:
                raise KeyError('project_id or project_name is required')
        else:
            raise KeyError('plan_id or plan_name is required')
        results = self.client.getTestPlanPlatforms(param)
        self._check_results(results)
        return results

    def _get_root_suites(self, **kwargs):
        """
        tl.getFirstLevelTestSuitesForTestProject
        :param kwargs: project_id, project_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        param = self.dev_key.copy()
        if project_id:
            param['testprojectid'] = project_id
        elif project_name:
            param['testprojectid'] = self._get_project_id(project_name=project_name)
        else:
            raise KeyError('project_id or project_name is required')
        results = self.client.getFirstLevelTestSuitesForTestProject(param)
        self._check_results(results)
        return results

    def _get_suites(self, **kwargs):
        """
        tl.getTestSuitesForTestSuite
        :param kwargs: project_name, project_id, suite_id, suite_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        suite_id = kwargs.get('suite_id')
        suite_name = kwargs.get('suite_name')
        param = self.dev_key.copy()
        if project_id:
            param['testprojectid'] = project_id
        elif project_name:
            param['testprojectid'] = self._get_project_id(project_name=project_name)
        else:
            raise KeyError('project_id or project_name is required')
        if suite_id:
            param['testsuiteid'] = suite_id
        elif suite_name:
            param['testsuiteid'] = self._get_suite_id(project_id=param['testprojectid'], suite_name=suite_name)
        else:
            raise KeyError('suite_id or suite_name is required')
        results = self.client.getTestSuitesForTestSuite(param)
        self._check_results(results)
        return results

    def _get_suite(self, **kwargs):
        """
        tl.getTestSuite
        :param kwargs: project_name, project_id, suite_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        suite_name = kwargs.get('suite_name')
        param = self.dev_key.copy()
        if project_id or project_name:
            param['prefix'] = self._get_project_prefix(project_name=project_name, project_id=project_id)
        else:
            raise KeyError('project_id or project_name is required')
        if suite_name:
            param['testsuitename'] = suite_name
        else:
            raise KeyError('suite_name is required')
        results = self.client.getTestSuite(param)
        self._check_results(results)
        return results

    def _get_suite_id(self, **kwargs):
        """

        :param kwargs: project_id, project_name, suite_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        suite_name = kwargs.get('suite_name')
        if not project_id and not project_name:
            raise KeyError('project_id or project_name is required')
        elif not suite_name:
            raise KeyError('suite_name is required')
        else:
            results = self._get_suite(project_name=project_name, project_id=project_id, suite_name=suite_name)
        if len(results) == 0:
            raise ValueError('No suite: %s in project: %s' % (suite_name, project_name if project_name else project_id))
        elif len(results) == 1:
            return results[0].get('id')
        else:
            ids = list()
            for result in results:
                ids.append(result.get('id'))
            raise ValueError('Find same name suites: %s %s in project: %s'
                             % (suite_name, ids, project_name if project_name else project_id))

    def _create_suite(self, **kwargs):
        """
        tl.createTestSuite
        :param kwargs: project_id, project_name, suite_name, parent_suite_name, parent_suite_id
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        suite_name = kwargs.get('suite_name')
        parent_suite_name = kwargs.get('parent_suite_name')
        parent_suite_id = kwargs.get('parent_suite_id')
        param = self.dev_key.copy()
        if project_id or project_name:
            param['prefix'] = self._get_project_prefix(project_name=project_name, project_id=project_id)
        else:
            raise KeyError('project_id or project_name is required')
        if suite_name:
            param['testsuitename'] = suite_name
        else:
            raise KeyError('suite_name is required')
        if parent_suite_id:
            param['parentid'] = parent_suite_id
        elif parent_suite_name:
            param['parentid'] = self._get_suite_id(project_name=project_name, project_id=project_id,
                                                   suite_name=parent_suite_name)
        results = self.client.createTestSuite(param)
        self._check_results(results)
        return results

    def _get_test_cases_for_suite(self, **kwargs):
        """
        tl.getTestCasesForTestSuite
        :param kwargs: project_id, project_name, suite_name, suite_id
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        suite_name = kwargs.get('suite_name')
        suite_id = kwargs.get('suite_id')
        param = self.dev_key.copy()
        if suite_id:
            param['testsuiteid'] = suite_id
        elif suite_name:
            if project_id or project_name:
                param['testsuiteid'] = self._get_suite_id(project_name=project_name, project_id=project_id,
                                                          suite_name=suite_name)
            else:
                raise KeyError('project_id or project_name is required')
        else:
            raise KeyError('suite_id or suite_name is required')
        return self.client.getTestCasesForTestSuite(param)

    def _get_test_cases_for_plan(self, **kwargs):
        """
        tl.getTestCasesForTestPlan
        :param kwargs: project_id, project_name, plan_name, plan_id, build_name, build_id, platform_id, platform_name
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        plan_id = kwargs.get('plan_id')
        plan_name = kwargs.get('plan_name')
        build_id = kwargs.get('build_id')
        build_name = kwargs.get('build_name')
        platform_id = kwargs.get('platform_id')
        platform_name = kwargs.get('platform_name')
        param = self.dev_key.copy()
        if plan_id:
            param['testplanid'] = plan_id
        elif plan_name:
            if project_id or project_name:
                param['testplanid'] = self._get_test_plan_id(project_name=project_name, project_id=project_id,
                                                             plan_name=plan_name)
            else:
                raise KeyError('project_id or project_name is required')
        else:
            raise KeyError('plan_id or plan_name is required')
        if build_id:
            param['buildid'] = build_id
        elif build_name:
            param['build_name'] = build_name
        if platform_id:
            param['platformid'] = platform_id
        elif platform_name:
            param['platformname'] = platform_name
        results = self.client.getTestCasesForTestPlan(param)
        self._check_results(results)
        return results

    def _get_test_case(self, **kwargs):
        """
        tl.getTestCase
        :param kwargs: project_id, project_name, case_ext_id
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        case_ext_id = kwargs.get('case_ext_id')
        param = self.dev_key.copy()
        if project_id:
            param['testprojectid'] = project_id
        elif project_name:
            param['testprojectid'] = self._get_project_id(project_name=project_name)
        else:
            raise KeyError('project_id or project_name is required')
        if case_ext_id:
            param['testcaseexternalid'] = case_ext_id
        else:
            raise KeyError('case_ext_id is required')
        results = self.client.getTestCase(param)
        self._check_results(results)
        return results

    def _create_test_case(self, **kwargs):
        """
        tl.createTestCase
        :param kwargs: project_id, project_name, suite_id, suite_name, case_name, summary, steps
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        suite_id = kwargs.get('suite_id')
        suite_name = kwargs.get('suite_name')
        case_name = kwargs.get('case_name')
        summary = kwargs.get('summary')
        steps = kwargs.get('steps')
        param = self.dev_key.copy()
        if project_id:
            param['testprojectid'] = project_id
        elif project_name:
            param['testprojectid'] = self._get_project_id(project_name=project_name)
        else:
            raise KeyError('project_id or project_name is required')
        if suite_id:
            param['testsuiteid'] = suite_id
        elif suite_name:
            param['testsuiteid'] = self._get_suite_id(project_name=project_name, project_id=project_id,
                                                      suite_name=suite_name)
        else:
            raise KeyError('suite_id or suite_name is required')
        if case_name:
            param['testcasename'] = case_name
        else:
            raise KeyError('case_name is required')
        param['authorlogin'] = self.user
        if summary:
            param['summary'] = summary
        else:
            param['summary'] = ''
        if steps:
            param['steps'] = steps
        else:
            param['steps'] = ''
        results = self.client.createTestCase(param)
        self._check_results(results)
        return results

    def _update_test_case_steps(self, **kwargs):
        """
        tl.createTestCaseSteps
        :param kwargs: case_ext_id, steps
        :return:
        """
        case_ext_id = kwargs.get('case_ext_id')
        steps = kwargs.get('steps')
        param = self.dev_key.copy()
        param['action'] = 'update'
        if case_ext_id:
            param['testcaseexternalid'] = case_ext_id
        else:
            raise KeyError('case_ext_id is required')
        if steps:
            param['steps'] = steps
        else:
            raise KeyError('steps is required')
        results = self.client.createTestCaseSteps(param)
        self._check_results(results)
        return results

    def _get_last_execution_result(self, **kwargs):
        """
        tl.getLastExecutionResult
        :param kwargs: project_id, project_name, plan_id, plan_name, build_id, build_name, platform_id, platform_name, case_ext_id
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        plan_id = kwargs.get('plan_id')
        plan_name = kwargs.get('plan_name')
        build_id = kwargs.get('build_id')
        build_name = kwargs.get('build_name')
        platform_id = kwargs.get('platform_id')
        platform_name = kwargs.get('platform_name')
        case_ext_id = kwargs.get('case_ext_id')
        param = self.dev_key.copy()
        if plan_id:
            param['testplanid'] = plan_id
        elif plan_name:
            if project_id or project_name:
                param['testplanid'] = self._get_test_plan_id(project_name=project_name, project_id=project_id,
                                                             plan_name=plan_name)
            else:
                raise KeyError('project_id or project_name is required')
        else:
            raise KeyError('plan_id or plan_name is required')
        if build_id:
            param['buildid'] = build_id
        elif build_name:
            param['buildname'] = build_name
        if platform_id:
            param['platformid'] = platform_id
        elif platform_name:
            param['platformname'] = platform_name
        if case_ext_id:
            param['testcaseexternalid'] = case_ext_id
        param['options'] = {'getBugs': True}
        results = self.client.getLastExecutionResult(param)
        self._check_results(results)
        return results

    def _get_all_execution_results(self, **kwargs):
        """
        Get all execution results
        :param kwargs: plan_id, case_ext_id
        :return:
        """
        plan_id = kwargs.get('plan_id')
        case_ext_id = kwargs.get('case_ext_id')
        param = self.dev_key.copy()
        if plan_id:
            param['testplanid'] = plan_id
        else:
            raise KeyError('plan_id is required')
        if case_ext_id:
            param['testcaseexternalid'] = case_ext_id
        else:
            raise KeyError('case_ext_id is required')
        param['options'] = {'getBugs': True}
        results = self.client.getAllExecutionsResults(param)
        self._check_results(results)
        return results

    def _set_case_execution_result(self, **kwargs):
        """
        tl.reportTCResult
        :param kwargs: project_id, project_name,
                       plan_id, plan_name,
                       build_id, build_name,
                       platform_id, platform_name,
                       case_ext_id,
                       case_exe_result,
                       notes
        :return:
        """
        project_id = kwargs.get('project_id')
        project_name = kwargs.get('project_name')
        plan_id = kwargs.get('plan_id')
        plan_name = kwargs.get('plan_name')
        build_id = kwargs.get('build_id')
        build_name = kwargs.get('build_name')
        platform_id = kwargs.get('platform_id')
        platform_name = kwargs.get('platform_name')
        case_ext_id = kwargs.get('case_ext_id')
        case_exe_result = kwargs.get('case_exe_result')
        notes = kwargs.get('notes')
        param = self.dev_key.copy()
        if plan_id:
            param['testplanid'] = plan_id
        elif plan_name:
            if project_id or project_name:
                param['testplanid'] = self._get_test_plan_id(project_name=project_name, project_id=project_id,
                                                             plan_name=plan_name)
            else:
                raise KeyError('project_id or project_name is required')
        else:
            raise KeyError('plan_id or plan_name is required')
        if platform_id:
            param['platformid'] = plan_id
        elif platform_name:
            param['platformname'] = platform_name
        else:
            raise KeyError('platform_id or platform_name is required')
        if build_id:
            param['buildid'] = build_id
        elif build_name:
            param['buildname'] = build_name
        else:
            raise KeyError('plan_id or plan_name is required')
        param['testcaseexternalid'] = case_ext_id
        if case_exe_result in ['p', 'f', 'b']:
            param['status'] = case_exe_result
        else:
            raise KeyError('case_exe_result is required and it should be p, f or b')
        if notes:
            param['notes'] = notes
        else:
            param['notes'] = ''
        results = self.client.reportTCResult(param)
        self._check_results(results)
        return results

    # Project Operations
    def get_issue_tracker(self, its_name: str):
        """
        Get Issue Tracker
        :param its_name: Issue Tracker System Name
        :return: issue_tracker_info
        """
        issue_tracker_info = {
            'uribase': '',
            'uriapi': '',
            'uriview': '',
        }
        its_info = self._get_issue_tracker(itsname=its_name).get('cfg')
        for its_key in issue_tracker_info.keys():
            try:
                issue_tracker_info[its_key] = its_info.split('<' + its_key + '>')[1].split('</' + its_key + '>')[0]
            except Exception as e:
                print(e)
        return issue_tracker_info

    def list_project(self):
        """
        List all projects
        :return:
        """
        projects = dict()
        for project in self._get_projects():
            projects[project.get('id')] = project.get('name')
        self._tree(projects.values())
        return projects

    # def get_project(self):
    #     pass

    def create_project(self, project_name: str, prefix=None):
        """
        Create project
        :param project_name:
        :param prefix:
        :return:
        """
        return self._create_project(project_name=project_name, prefix=prefix)[0].get('id')

    def delete_project(self, project_name: str):
        """
        Delete project
        :param project_name:
        :return:
        """
        return self.delete_project(project_name=project_name)

    def list_requirement(self, project_name: str = '', plan_name: str = '', platform_name: str = '', **kwargs):
        """
        Get Requirements From The Project [Plan Platform]
        :param project_name:
        :param plan_name:
        :param platform_name:
        :param kwargs: project_id, plan_id, platform_id
        :return:
            {req_id: req_doc_id}
        """
        project_id = kwargs.get('project_id')
        plan_id = kwargs.get('plan_id')
        platform_id = kwargs.get('platform_id')
        reqs = dict()
        for req in self._get_requirements(project_name=project_name, project_id=project_id,
                                          plan_name=plan_name, plan_id=plan_id,
                                          platform_name=platform_name, platform_id=platform_id):
            reqs[req.get('id')] = req.get('req_doc_id')
        return reqs

    def get_requirement(self, project_name: str = '', requirement_doc_id: str = '', **kwargs):
        """
        Get Case List From The Requirement
        :param project_name:
        :param requirement_doc_id:
        :param kwargs: project_id
        :return:
            {case_external_id: case_name}
        """
        project_id = kwargs.get('project_id')
        cases = dict()
        prefix = self._get_project_prefix(project_name=project_name, project_id=project_id)
        for case in self._get_requirement_coverage(project_name=project_name, project_id=project_id,
                                                   requirement_doc_id=requirement_doc_id):
            cases['%s-%s' % (prefix, case.get('tc_external_id'))] = case.get('name')
        return cases

    # Plan Operations
    def list_plan(self, project_name: str = '', **kwargs):
        """
        Get Plan List From The Project
        :param project_name:
        :param kwargs: project_id
        :return:
            {plan_id: plan_name}
        """
        project_id = kwargs.get('project_id')
        plans = dict()
        for testplan in self._get_project_test_plans(project_name=project_name, project_id=project_id):
            plans[testplan.get('id')] = testplan.get('name')
        self._tree(plans.values(), root=project_name)
        return plans

    def get_plan(self, project_name: str = '', plan_name: str = '', build_name: str = '', platform_name: str = '',
                 requirement_doc_id: str = '', **kwargs):
        """
        Get Case Execution Results From The Plan
        :param project_name:
        :param plan_name:
        :param build_name:
        :param platform_name:
        :param requirement_doc_id:
        :param kwargs: project_id, plan_id, build_id, platform_id
        :return: cases info
            {
                case_external_id: {
                    'case_name': case_name,
                    'exec_status': exec_status,
                    'bugs': [bug_id],
                }
            }
        """
        project_id = kwargs.get('project_id')
        plan_id = kwargs.get('plan_id')
        build_id = kwargs.get('build_id')
        platform_id = kwargs.get('platform_id')
        if not plan_id:
            plan_id = self._get_test_plan_id(project_name=project_name, project_id=project_id, plan_name=plan_name)
        testcases = dict()
        cases = self._get_test_cases_for_plan(project_name=project_name, project_id=project_id,
                                              plan_name=plan_name, plan_id=plan_id,
                                              build_name=build_name, build_id=build_id,
                                              platform_name=platform_name, platform_id=platform_id)
        req_cases = self.get_requirement(project_name=project_name, project_id=project_id,
                                         requirement_doc_id=requirement_doc_id).keys() if requirement_doc_id else []
        for testcase in cases.values():
            tc = testcase[sorted(testcase.keys())[0]]
            tc_id = tc.get('full_external_id')
            if requirement_doc_id and tc_id not in req_cases:
                continue
            tc_bugs = list()
            if tc.get('exec_status') in ['f', 'b']:
                for bid in self.get_all_execution_result(plan_id=plan_id, case_ext_id=tc_id).get('bugs'):
                    tc_bugs.append(bid.get('bug_id'))
            testcases[tc_id] = {
                'case_name': tc.get('tcase_name'),
                'exec_status': tc.get('exec_status'),
                'bugs': tc_bugs,
            }
        self._tree(testcases, root=plan_name)
        return testcases

    def list_build(self, project_name: str = '', plan_name: str = '', **kwargs):
        """
        List all builds
        :param project_name:
        :param plan_name:
        :param kwargs: project_id, plan_id
        :return: builds info
        """
        project_id = kwargs.get('project_id')
        plan_id = kwargs.get('plan_id')
        builds = dict()
        results = self._get_builds_for_plan(project_name=project_name, project_id=project_id,
                                            plan_name=plan_name, plan_id=plan_id)
        for result in results:
            builds[result.get('id')] = result.get('name')
        return builds

    def list_platform(self, project_name: str = '', plan_name: str = '', **kwargs):
        """
        List all platforms
        :param project_name:
        :param plan_name:
        :param kwargs: project_id, plan_id
        :return: platforms info
        """
        project_id = kwargs.get('project_id')
        plan_id = kwargs.get('plan_id')
        platforms = dict()
        results = self._get_platforms_for_plan(project_name=project_name, project_id=project_id,
                                               plan_name=plan_name, plan_id=plan_id)
        for result in results:
            platforms[result.get('id')] = result.get('name')
        return platforms

    # def create_plan(self):
    #     pass
    #
    # def delete_plan(self):
    #     pass

    # Suite Operations
    def list_suite(self, project_name: str = '', suite_name: str = '', **kwargs):
        """
        List all suites
        :param project_name:
        :param suite_name:
        :param kwargs: project_id, suite_id
        :return: suites info { suite_id: suite_name}
        """
        project_id = kwargs.get('project_id')
        suite_id = kwargs.get('suite_id')
        suites = dict()
        if suite_id or suite_name:
            for suite in self._get_suites(project_name=project_name, project_id=project_id,
                                          suite_name=suite_name, suite_id=suite_id).values():
                suites[suite.get('id')] = suite.get('name')
        else:
            for suite in self._get_root_suites(project_name=project_name, project_id=project_id):
                suites[suite.get('id')] = suite.get('name')
        # names = list()
        # if suite_name:
        #     for suite in self._get_root_suites(project_name):
        #         names.append(suite.get('name'))
        # else:
        #     results = self._get_suites(project_name, suite_name, suite_id)
        #     for suite in results:
        #         names.append(results.get(suite).get('name'))
        self._tree(suites.values())
        return suites

    def get_suite(self, project_name: str = '', suite_name: str = '', **kwargs):
        """
        Get suite information
        :param project_name:
        :param suite_name:
        :param kwargs: project_id, suite_id
        :return: cases info { external_id: name}
        """
        project_id = kwargs.get('project_id')
        suite_id = kwargs.get('suite_id')
        testcases = dict()
        cases = self._get_test_cases_for_suite(project_name=project_name, project_id=project_id,
                                               suite_name=suite_name, suite_id=suite_id)
        for testcase in cases:
            testcases[testcase.get('external_id')] = testcase.get('name')
        self._tree(testcases, root=suite_name)
        return testcases

    def create_suite(self, project_name: str = '', suite_name: str = '', parent_suite_name: str = '', **kwargs):
        """
        Create suite
        :param project_name:
        :param suite_name:
        :param parent_suite_name:
        :param kwargs: project_id, suite_id, parent_suite_id
        :return: case external ID
        """
        project_id = kwargs.get('project_id')
        # suite_id = kwargs.get('suite_id')
        parent_suite_id = kwargs.get('parent_suite_id')
        return self._create_suite(project_name=project_name, project_id=project_id, suite_name=suite_name,
                                  parent_suite_name=parent_suite_name, parent_suite_id=parent_suite_id)[0].get('id')

    # Case Operations
    def list_case(self, project_name: str = '', suite_name: str = '', **kwargs):
        """
        List all cases
        :param project_name:
        :param suite_name:
        :param kwargs: project_id, suite_id
        :return: cases info { external_id: name}
        """
        project_id = kwargs.get('project_id')
        suite_id = kwargs.get('suite_id')
        return self.get_suite(project_name=project_name, project_id=project_id,
                              suite_name=suite_name, suite_id=suite_id)

    def get_case(self, project_name: str = '', case_ext_id: str = '', **kwargs):
        """
        Get case information
        :param project_name:
        :param case_ext_id:
        :param kwargs: project_id
        :return:
        """
        project_id = kwargs.get('project_id')
        return self._get_test_case(project_name=project_name, project_id=project_id, case_ext_id=case_ext_id)

    def create_case(self, project_name: str = '', suite_name: str = '', case_name: str = '',
                    summary='', steps='', **kwargs):
        """
        Create test case
        :param project_name:
        :param suite_name:
        :param case_name:
        :param summary:
        :param steps:
        :param kwargs: project_id, suite_id
        :return: case external ID
        """
        project_id = kwargs.get('project_id')
        suite_id = kwargs.get('suite_id')
        results = self._create_test_case(project_id=project_id, project_name=project_name,
                                         suite_id=suite_id, suite_name=suite_name,
                                         case_name=case_name, summary=summary, steps=steps)
        case_id = {
            'id': results[0]['additionalInfo']['id'],
            'external_id': results[0]['additionalInfo']['external_id'],
        }
        prefix = self._get_project_prefix(project_name=project_name, project_id=project_id)
        print('ID: %s | External ID: %s-%s | Case Title: %s'
              % (case_id['id'], prefix, case_id['external_id'], case_name))
        return case_id

    def update_step(self, case_ext_id: str, steps):
        """
        Update test case steps
        :param case_ext_id:
        :param steps:
        :return:
        """
        feedback = self._update_test_case_steps(case_ext_id=case_ext_id, steps=steps).get('feedback')
        results = dict()
        for item in feedback:
            _operation = item.get('operation')
            if _operation not in results.keys():
                results[_operation] = list()
            results[_operation].append(item.get('step_number'))
        show_str = 'External ID: %s' % case_ext_id
        for step_operation in results.keys():
            show_str = ' | '.join([
                show_str,
                '%s Step Number: %s' % (step_operation.upper(), results.get(step_operation))
            ])
        print(show_str)
        return feedback

    def set_execution_result(self, project_name: str = '', plan_name: str = '',
                             platform_name: str = '', build_name: str = '',
                             case_ext_id: str = '', case_exe_result: str = '', notes='', **kwargs):
        """
        Set execution result into test case
        :param project_name:
        :param plan_name:
        :param platform_name:
        :param build_name:
        :param case_ext_id:
        :param case_exe_result:
        :param notes:
        :param kwargs: project_id, plan_id, platform_id, build_id
        :return:
        """
        project_id = kwargs.get('project_id')
        plan_id = kwargs.get('plan_id')
        platform_id = kwargs.get('platform_id')
        build_id = kwargs.get('build_id')
        if case_exe_result.lower() in ['p', 'pass', 'passed']:
            case_exe_result = 'p'
        elif case_exe_result.lower() in ['f', 'fail', 'failed']:
            case_exe_result = 'f'
        elif case_exe_result.lower() in ['b', 'block', 'blocked']:
            case_exe_result = 'b'
        rc_result = self._set_case_execution_result(project_name=project_name, project_id=project_id,
                                                    plan_name=plan_name, plan_id=plan_id,
                                                    platform_name=platform_name, platform_id=platform_id,
                                                    build_name=build_name, build_id=build_id,
                                                    case_ext_id=case_ext_id, case_exe_result=case_exe_result,
                                                    notes=notes)
        return rc_result[0].get('message')

    def get_last_execution_result(self, project_name: str = '', plan_name: str = '', build_name: str = '',
                                  platform_name: str = '', case_ext_id: str = '', **kwargs):
        """
        Get the last execution result
        :param project_name:
        :param plan_name:
        :param build_name:
        :param platform_name:
        :param case_ext_id:
        :param kwargs: project_id, plan_id, build_id, platform_id
        :return:
        """
        project_id = kwargs.get('project_id')
        plan_id = kwargs.get('plan_id')
        build_id = kwargs.get('build_id')
        platform_id = kwargs.get('platform_id')
        last_results = dict()
        exe_results = self._get_last_execution_result(
            project_name=project_name, project_id=project_id,
            plan_name=plan_name, plan_id=plan_id,
            build_name=build_name, build_id=build_id,
            platform_name=platform_name, platform_id=platform_id,
            case_ext_id=case_ext_id)
        for exe_result in exe_results:
            last_results[exe_result.get('testcaseexternalid')] = exe_result.get('status') \
                if exe_result.get('status') else 'n'
        self._tree(last_results.values())
        return last_results

    def get_all_execution_result(self, plan_id, case_ext_id):
        """
        Get all execution results
        :param plan_id:
        :param case_ext_id:
        :return:
        """
        all_results = self._get_all_execution_results(plan_id=plan_id, case_ext_id=case_ext_id)
        for key, value in all_results.items():
            return value

    # Report Operation
    def get_report_for_plan(self, project_name: str = '', plan_name: str = '',
                            build_name: str = '', platform_name: str = '', **kwargs):
        """
        Get test report for the plan
        :param project_name:
        :param plan_name:
        :param build_name:
        :param platform_name:
        :param kwargs: project_id, plan_id, build_id, platform_id
        :return:
        """
        project_id = kwargs.get('project_id')
        plan_id = kwargs.get('plan_id')
        build_id = kwargs.get('build_id')
        platform_id = kwargs.get('platform_id')
        last_report = dict()
        last_executed = list()
        cases = self.get_plan(project_id=project_id, project_name=project_name,
                              plan_name=plan_name, plan_id=plan_id,
                              build_name=build_name, build_id=build_id,
                              platform_name=platform_name, platform_id=platform_id)
        for value in cases.values():
            last_executed.append(value.get('exec_status'))
        last_report['notrun'] = last_executed.count('n')
        last_report['pass'] = last_executed.count('p')
        last_report['fail'] = last_executed.count('f')
        last_report['block'] = last_executed.count('b')
        print(last_report)
        last_report['case'] = cases
        return last_report


if __name__ == '__main__':
    print('This is TestLink XML-RPC client')
