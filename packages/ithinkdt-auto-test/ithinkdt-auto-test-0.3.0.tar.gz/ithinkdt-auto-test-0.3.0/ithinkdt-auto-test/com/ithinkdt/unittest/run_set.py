"""
读取TXT文件中的要运行的测试模块，并按顺序执行
"""
import os
import unittest


class RunSet:
    # 初始化 先有实例，才能初始化
    def __init__(self, root_path):
        """
        加载测试用例初始化
        :param root_path: 项目的主路径
        """
        self.root_path = root_path
        # 项目主路径
        self.ROOT_PATH = self.root_path
        # 测试用例方法路径
        self.CASE_PATH = os.path.join(self.ROOT_PATH, 'testCase')

    def set_case_list(self):
        """读取TXT文件中的运行模块，返回列表"""
        case_list = []
        case_list_path = os.path.join(self.ROOT_PATH, "caseList.txt")
        fb = open(case_list_path, encoding='UTF-8')
        for case in fb.readlines():
            case_name = str(case)
            if case_name != "" and not case_name.startswith("#"):
                case_list.append(case_name.replace("\n", ""))
        fb.close()
        return case_list

    def set_suite(self):
        """循环测试用例的列表，用名字匹配testCase下的py文件，加载测试用例"""
        suite_list = unittest.TestSuite()
        suite_module = []
        case_list = self.set_case_list()

        for case in case_list:
            case_name = str(case)
            # TestLoader类中提供的discover（）方法可以自动识别测试用例,
            # pattern=：表示用例文件名的匹配原则。此处匹配以“ ”开头的.py 类型的文件
            discover = unittest.defaultTestLoader.discover(self.CASE_PATH, pattern=case_name + '.py', top_level_dir=None)
            if len(discover._tests) != 0:
                suite_module.append(discover)
        if len(suite_module) > 0:
            for case in suite_module:
                suite_list.addTest(case)  # 通过TestSuite类的addTest（）方法按照一定的顺序来加载
        else:
            return None
        return suite_list
