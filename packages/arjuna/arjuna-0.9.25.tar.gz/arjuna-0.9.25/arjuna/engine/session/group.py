# This file is a part of Arjuna
# Copyright 2015-2020 Rahul Verma

# Website: www.RahulVerma.net

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import pytest

from arjuna.core.error import TestGroupsFinished
from arjuna.core.constant import *
from arjuna.tpi.constant import *


class TestGroup:

    def __init__(self, *, name, config, session, stage, im=None, em=None, it=None, et=None):
        self.__name = name
        self.__session = session
        self.__stage = stage
        self.__config = config
        self.__thname = None
        self.__dry_run = session.dry_run
        self.__filters = {'im' : im, 'em': em, 'it': it, 'et': et}

    @property
    def config(self):
        return self.__config

    @property
    def thread_name(self):
        return self.__thname

    @thread_name.setter
    def thread_name(self, name):
        self.__thname = name

    @property
    def tests_dir(self):
        return self.__tests_dir

    def run(self):
        from arjuna import Arjuna
        from arjuna.tpi.constant import ArjunaOption
        Arjuna.register_group_params(name=self.__name, config=self.__config, thread_name=self.thread_name)
        self.__load_command_line()

        os.chdir(self.__project_dir)
        print("Executing pytest with args: {}".format(" ".join(self.__pytest_args)))


        pytest_retcode = pytest.main(self.__pytest_args)
        return pytest_retcode

    def __load_command_line(self):
        from arjuna import Arjuna
        from arjuna.tpi.constant import ArjunaOption
        self.__project_dir = self.config.value(ArjunaOption.PROJECT_ROOT_DIR)
        # import sys
        # sys.path.insert(0, self.__project_dir + "/..")
        self.__tests_dir = self.config.value(ArjunaOption.TESTS_DIR)
        suffix = ""
        if self.__name != "mgroup":
            suffix = "-" + self.__session.name + "-" + self.__stage.name + "-" + self.__name
        self.__xml_path = os.path.join(self.config.value(ArjunaOption.REPORT_XML_DIR), "report{}.xml".format(suffix))
        self.__html_path = os.path.join(self.config.value(ArjunaOption.REPORT_HTML_DIR), "report{}.html".format(suffix))
        self.__report_formats = self.config.value(ArjunaOption.REPORT_FORMATS)
        # self.__report_formats = Value.as_enum_list(rfmts, ReportFormat)
        res_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../res"))
        pytest_ini_path = res_path + "/pytest.ini"

        # -s is to print to console.
        self.__pytest_args = ["-c", pytest_ini_path, "--rootdir", self.__project_dir, "--no-print-logs", "--show-capture", "all", "--disable-warnings"] # 
        self.__test_args = []
        self.__load_tests(**self.__filters)
        self.__load_meta_args()


    def __load_tests(self, *, im=None, em=None, it=None, et=None):
        if im is None and em is None and it is None and et is None:
            self.__load_all_tests()
        else:
            self.__load_tests_from_pickers(im=im, em=em, it=it, et=et)

    def __load_all_tests(self):
        self.__pytest_args.insert(0, self.tests_dir)

    def __load_tests_from_pickers(self, *, im=None, em=None, it=None, et=None):  

        def process_modules(ms):
            ms = [m.replace(".py", "").replace("*","").replace("/", " and ").replace("\\", " and ") for m in ms]
            return ["and" in m and "({})".format(m) or m for m in ms]

        k_args = []

        k_flag = False

        if em:            
            em = process_modules(em)
            k_args.append(" and ".join(["not " + m for m in em]))
            k_flag = True

        # if ic:
        #     prefix = k_flag and " and " or ""
        #     k_args.append(prefix + " and ".join(["not " + c for c in ic]))
        #     k_flag = True

        if et:
            prefix = k_flag and " and " or ""
            k_args.append(prefix + " and ".join(["not " + c for c in et]))
            k_flag = True

        if im:
            prefix = k_flag and " and " or ""            
            cm = process_modules(im)
            k_args.append(prefix + " or ".join(im))
            k_flag = True

        # if cc:
        #     prefix = k_flag and " and " or "" 
        #     k_args.append(prefix + " or ".join(cc))
        #     k_flag = True

        if it:
            prefix = k_flag and " and " or "" 
            k_args.append(prefix + " or ".join(it))
            k_flag = True

        if k_flag:
            self.__test_args.append("-k " + "".join(k_args))

    def __load_meta_args(self):
        pytest_report_args = []

        if ReportFormat.XML in self.__report_formats:
            pytest_report_args.extend(["--junit-xml", self.__xml_path])

        if ReportFormat.HTML in self.__report_formats:
            pytest_report_args.extend(["--html", self.__html_path, "--self-contained-html"])

        self.__pytest_args.extend(pytest_report_args)
        self.__pytest_args.extend(self.__test_args)

        if self.__dry_run not in {False, None}:
            print("!!!!!! This is a DRY RUN !!!!!!!")
            if self.__dry_run == DryRunType.SHOW_TESTS:
                print("Dry Run Type: SHOW TESTS")
                print("You can see the test functions which will be executed as per settings of your command.")
                self.__pytest_args.extend(["--collect-only"])
            elif self.__dry_run == DryRunType.SHOW_PLAN:
                print("Dry Run Type: SHOW PLAN")
                print("You can see the test functions as well as the fixtures which will be executed as per settings of your command.")
                self.__pytest_args.extend(["--setup-plan"])
            elif self.__dry_run == DryRunType.RUN_FIXTURES:
                print("Dry Run Type: RUN FIXTURES")
                print("All fixtures will be executed as per your current command. You can see the test functions which will be executed as per settings of your command.")
                self.__pytest_args.extend(["--setup-only"])

    def __str__(self):
        return "Command: config={}, group={}, pickers={}".format(self.config.name, self.__name, self.__filters)


class YamlTestGroup(TestGroup):

    def __init__(self, *, group_yaml, session, stage):
        self.__config = stage.config
        self.__filters = {
            'im': None,
            'em': None,
            'it': None,
            'et': None
        }
        self.__process_yaml(group_yaml)
        super().__init__(name=group_yaml.name, config=self.__config, session=session, stage=stage, **self.__filters)

    def __process_yaml(self, group_yaml):
        from arjuna import Arjuna
        for gmd_name in group_yaml.section_names:
            if gmd_name.lower() == "conf":
                self.__config = Arjuna.get_config(group_yaml.get_value("conf"))
            elif gmd_name.lower() in {'im', 'em', 'it', 'et'}:
                self.__filters[gmd_name.lower()] = group_yaml.get_value(gmd_name)

class MagicTestGroup(TestGroup):

    def __init__(self, *, session, stage, im=None, em=None, it=None, et=None):
        super().__init__(name="mgroup", config=stage.config, session=session, stage=stage, im=im, em=em, it=it, et=et)


class TestGroups:

    def __init__(self):
        self.__names = []
        self.__iter = None

    def add_group(self, group):
        self.__names.append(group)

    def freeze(self):
        self.__iter = iter(self.__names)

    def __iter__(self):
        return self

    def next(self):
        try:
            return next(self.__iter)
        except StopIteration:
            raise TestGroupsFinished()

    def __str__(self):
        return str([str(c) for c in self.__names])