# coding=utf-8
"""

``fish_file`` 包含的是文件、路径处理相关的函数。

各类相对绝对文件的路径处理等都是开发时候经常需要处理的问题，fish_file 中的函数试图简化这些操作。

"""

# 2017.1.8 v1.0.9 created

import chardet
import pathlib
import os


# 生成当前路径下一级路径某文件的完整文件名
# ---
# 2016.4.7 v1.0.6, v1.0.7, create by David Yi
# 2017.1.8 v1.0.9 edit the function name, #19002
# 2018.1.30 1.31 v1.0.10 代码优化, #11004
# 2018.4.24 v1.0.11 加入 docstring
# 2018.5.28 v1.0.13 edit, #19040
# 2019.4.1 v1.1.8 edit by Hu Jun, #218
def get_abs_filename_with_sub_path(sub_path, filename):

    """
        生成当前路径下一级路径某文件的完整文件名；

        :param:
            * sub_path: (string) 下一级的某路径名称
            * filename: (string) 下一级路径的某个文件名
        :returns:
            * 返回类型 (tuple)，有两个值，第一个为 flag，第二个为文件名，说明见下
            * flag: (bool) 如果文件存在，返回 True，文件不存在，返回 False
            * abs_filename: (string) 指定 filename 的包含路径的长文件名

        举例如下::
            
            print('--- get_abs_filename_with_sub_path demo ---')
            # define sub dir
            path_name = 'sub_dir'
            # define not exists file
            filename = 'test_file.txt'

            abs_filename = get_abs_filename_with_sub_path(path_name, filename)
            # return False and abs filename
            print(abs_filename)

            # define exists file
            filename = 'demo.txt'
            abs_filename = get_abs_filename_with_sub_path(path_name, filename)
            # return True and abs filename
            print(abs_filename)
            print('---')

        输出结果::
            
            --- get_abs_filename_with_sub_path demo ---
            (False, '/Users/****/Documents/dev_python/fishbase/demo/sub_dir/test_file.txt')
            (True, '/Users/****/Documents/dev_python/fishbase/demo/sub_dir/demo.txt')
            ---
            
    """

    try:
        cur_path = pathlib.Path.cwd()
        abs_filename = cur_path / pathlib.Path(sub_path) / filename
        flag = pathlib.Path.is_file(abs_filename)

        # 将 path 对象转换成字符串
        return flag, str(abs_filename)

    except:

        flag = False
        return flag, None


# 判断文件名是否没有输入后缀，没有的话则加上后缀
# create 2015.8.1 by David Yi
# edit 2018.6.3 v1.0.13, #19044
# def check_ext_add(filename, ext):
#
#     temp_filename = filename
#     if os.path.splitext(temp_filename)[1] == '':
#         temp_filename += ext
#
#     return temp_filename


# 检查当前路径下的某个子路径是否存在, 不存在则创建
# 2016.10.4 v1.0.9 #19001, edit by David Yi
# 2018.5.28 v1.0.13 #19042, edit by David Yi
# 2019.4.1 v1.1.8 edit by Hu Jun, #218
def check_sub_path_create(sub_path):

    """
    检查当前路径下的某个子路径是否存在, 不存在则创建；

    :param:
        * sub_path: (string) 下一级的某路径名称
    :return:
        * 返回类型 (tuple)，有两个值
        * True: 路径存在，False: 不需要创建
        * False: 路径不存在，True: 创建成功

    举例如下::
        
        print('--- check_sub_path_create demo ---')
        # 定义子路径名称
        sub_path = 'demo_sub_dir'
        # 检查当前路径下的一个子路径是否存在，不存在则创建
        print('check sub path:', sub_path)
        result = check_sub_path_create(sub_path)
        print(result)
        print('---')

    输出结果::
        
        --- check_sub_path_create demo ---
        check sub path: demo_sub_dir
        (True, False)
        ---
        
    """

    # 获得当前路径
    temp_path = pathlib.Path()
    cur_path = temp_path.resolve()

    # 生成 带有 sub_path_name 的路径
    path = cur_path / pathlib.Path(sub_path)

    # 判断是否存在带有 sub_path 路径
    if path.exists():
        # 返回 True: 路径存在, False: 不需要创建
        return True, False
    else:
        path.mkdir(parents=True)
        # 返回 False: 路径不存在  True: 路径已经创建
        return False, True


# 2019.4.1 v1.1.10 edit by Hu Jun, #226
def get_file_encoding(file_path):

    """
    获取给定文件的编码；

    :param:
        * file_path: (string) 文件的完整路径
    :return:
        * file_encoding (string)，文件编码

    举例如下::

        print('--- get_file_encoding demo ---')
        result = get_file_encoding(__file__)
        print(result)
        print('---')

    输出结果::

        --- get_file_encoding demo ---
        utf-8
        ---

        """
    # 判断给定路径是否是一个文件
    flag = pathlib.Path(file_path).is_file()
    if not flag:
        raise RuntimeError('file {}, does not exist'.format(file_path))

    # 读入文件
    with open(file_path, 'rb') as f:
        buf = f.read()
        # 获取文件信息
        file_info = chardet.detect(buf)
        
        encoding = file_info['encoding']
        if encoding.startswith(('utf-8', 'UTF-8')):
            file_encoding = encoding
        else:
            file_encoding = 'GB2312'
        return file_encoding


# v1.0.14 edit by Hu Jun, edit by Jia Chunying, #38
# v1.0.17 edit by Hu Jun, #212
# v1.3 edit by David Yi, #272
def find_files(path, exts=None):
    """
    查找路径下的文件，返回指定类型的文件列表

    :param:
        * path: (string) 查找路径
        * exts: (list) 文件类型列表，默认为空

    :return:
        * files_list: (list) 文件列表

    举例如下::

        print('--- find_files demo ---')
        path1 = '/root/fishbase_issue'
        all_files = find_files(path1)
        print(all_files)
        exts_files = find_files(path1, exts=['.png', '.py'])
        print(exts_files)
        print('---')

    执行结果::

        --- find_files demo ---
        ['/root/fishbase_issue/test.png', '/root/fishbase_issue/head.jpg','/root/fishbase_issue/py/man.png'
        ['/root/fishbase_issue/test.png', '/root/fishbase_issue/py/man.png']
        ---

        """
    files_list = []
    for root, dirs, files in os.walk(path):
        for name in files:
            files_list.append(os.path.join(root, name))

    if exts is not None:
        return [file for file in files_list if pathlib.Path(file).suffix in exts]

    return files_list

# 生成使用模块时的下一级路径某文件的完整文件名
# 2016.5.18 create by David Yi
# 2017.1.8 v1.0.9 edit the function name, #19004
# 2018.4.24 v1.0.11 增加 docstring 支持
# def get_abs_filename_with_sub_path_module(sub_path, filename):
#
#     """
#     生成使用模块时的下一级路径某文件的完整文件名；
#
#     :param:
#         * sub_path: (string) 下一级的某路径名称
#         * filename: (string) 下一级路径的某个文件名
#     :return:
#         * 返回类型 (tuple)，有两个值，第一个为 flag，第二个为文件名，说明见下
#         * flag: (bool) 如果文件存在，返回 True，文件不存在，返回 False
#         * abs_filename: (string) 指定 filename 的包含路径的长文件名，注意是模块安装的路径，不是应用程序的路径
#
#     举例如下::
#
#         # 定义子路径名称
#         sub_path = 'test_sub_dir'
#         # 定义存在的文件名称
#         filename_existent = 'demo_file.txt'
#         # 定义不存在的文件名称
#         filename_non_existent = 'demo.txt'
#         # 生成下一级路径文件的完整文件名
#         result = get_abs_filename_with_sub_path_module(sub_path, filename_existent)
#         print(result)
#
#         result = get_abs_filename_with_sub_path_module(sub_path, filename_non_existent)
#         print(result)
#
#     输出结果::
#
#         (True, '/Users/*****/anaconda3/lib/python3.6/site-packages/fishbase/test_sub_dir/demo_file.txt')
#         (False, '/Users/****/anaconda3/lib/python3.6/site-packages/fishbase/test_sub_dir/demo.txt')
#     """
#
#     cur_module_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#     abs_filename = os.path.join(cur_module_dir, sub_path, filename)
#
#     # 检查是否存在文件名
#     if os.path.exists(abs_filename):
#         return True, abs_filename
#     else:
#         return False, abs_filename
