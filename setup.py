# from distutils.core import setup
# import py2exe

# setup(
#     console=['Main.py'],
#     packages=['Common', 'Foo'],
#     options={
#         'py2exe': {
#             'packages': ['Common', 'Foo'],
#             'includes': ['Common.tool', 'os', 'Foo.foo'],  # os.pathを含める
#             'dll_excludes': ['MSVCP90.dll'],  # 不要なDLLを除外
#         }
#     }
# )

from cx_Freeze import setup, Executable

setup(
    name="YourAppName",
    version="1.0",
    description="Your application description",
    executables=[Executable("Main.py")],
)

