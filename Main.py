import tkinter_example.script1 as sc
import Common.tool as tl
import Foo.foo as fo

def some_function():
    print("Function called.")

if __name__ == '__main__':
    # 直接実行された場合にのみ実行されるコード
    some_function()
    tl.main()
    fo.foo()
    sc.main()
    app = fo.MakeGraph()
    app.make_graph()
    d = input('Press Any key.')