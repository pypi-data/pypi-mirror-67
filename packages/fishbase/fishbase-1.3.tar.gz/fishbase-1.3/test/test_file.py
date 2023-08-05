# coding=utf-8
# fish_file.py 单元测试
# 2018.5.28 create by David Yi

import os
import pytest
from fishbase.fish_file import *

# 定义当前路径
current_path = os.path.dirname(os.path.abspath(__file__))
# 定义配置文件名
test_filename = os.path.join(current_path, 'test_gb2312_encoding.txt')


# 2018.5.28 v1.0.13 #19040,#19042, create by David Yi, fish_file unittest
class TestFishFile(object):

    # tc for get_abs_filename_with_sub_path()
    def test_get_abs_filename_with_sub_path_01(self):

        # 定义子路径名称
        path_name_0 = os.path.join(current_path, '..', 'test')
        path_name_1 = os.path.join(current_path, '..', 'test01')
        # 定义文件名称
        filename_0 = 'readme.111'
        filename_1 = 'test_file.py'

        # tc
        result = get_abs_filename_with_sub_path(path_name_0, filename_0)
        assert result[0] is False

        result = get_abs_filename_with_sub_path(path_name_0, filename_1)
        assert result[0] is True
        # print(result[1])

        abs_file = os.path.join(os.path.abspath(''), path_name_0, filename_1)
        assert result[1] == abs_file

        result = get_abs_filename_with_sub_path(path_name_1, filename_0)
        assert result[0] is False

        result = get_abs_filename_with_sub_path(path_name_1, filename_1)
        assert result[0] is False

    # tc for check_sub_path_create()
    def test_check_sub_path_create_01(self):

        # 定义子路径名
        sub_path = 'test_sub_path'
        # 获得完整路径名
        cur_path = os.getcwd()
        abs_path = os.path.join(cur_path, sub_path)

        # 如果存在该子路径，先删除
        if os.path.isdir(abs_path):
            os.rmdir(abs_path)

        # tc 不存在子路径，创建检查
        result = check_sub_path_create(sub_path)
        assert result[0] is False
        assert result[1] is True

        os.rmdir(abs_path)

        # tc 存在子路径，不创建检查
        os.makedirs(abs_path)
        result = check_sub_path_create(sub_path)
        assert result[0] is True
        assert result[1] is False

        # 删除临时文件
        os.rmdir(abs_path)

    # tc for get_file_encoding()
    def test_get_file_encoding_01(self):
        assert get_file_encoding(__file__) == 'utf-8'
        # 应该读不到返回的 dict 内容
        with pytest.raises(RuntimeError):
            temp_file = __file__ + '.for_test'
            get_file_encoding(temp_file)
        
        gbk_file_path = test_filename
        assert get_file_encoding(gbk_file_path) == 'GB2312'

    # test find_files() tc
    def test_find_files_01(self):
        path = './'
        exts_list = ['.ini', '.py']

        assert len(find_files(path)) >= len(find_files(path, exts=exts_list))

