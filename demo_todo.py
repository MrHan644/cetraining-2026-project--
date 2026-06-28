#!/usr/bin/env python3
"""
待办事项管理器演示脚本
展示所有核心功能的使用方法
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from todo_manager import TodoManager, Priority

def demo_basic_operations():
    """演示基本操作"""
    print("=" * 60)
    print("待办事项管理器功能演示")
    print("=" * 60)

    # 创建管理器（使用临时文件，避免影响真实数据）
    manager = TodoManager("demo_todos.json")

    print("\n1. 添加待办事项")
    print("-" * 40)

    # 添加一些示例待办事项
    manager.add_todo("完成项目报告", "高", "2026-06-25")
    manager.add_todo("购买 groceries", "中", "2026-06-24")
    manager.add_todo("学习 Python", "低")
    manager.add_todo("紧急会议", "紧急", "2026-06-23")
    manager.add_todo("阅读书籍", "低", "2026-06-30")

    print("\n2. 查看所有待办事项（按ID排序）")
    print("-" * 40)
    todos = manager.list_todos(sort_by="id", filter_status="全部")
    for todo in todos:
        print(f"  {todo}")

    print("\n3. 查看待办事项（按优先级排序）")
    print("-" * 40)
    todos = manager.list_todos(sort_by="priority", filter_status="全部")
    for todo in todos:
        print(f"  {todo}")

    print("\n4. 查看未完成的待办事项")
    print("-" * 40)
    todos = manager.list_todos(sort_by="id", filter_status="未完成")
    for todo in todos:
        print(f"  {todo}")

    print("\n5. 标记待办事项为已完成")
    print("-" * 40)
    # 标记前3个待办事项为已完成
    for i in range(1, 4):
        manager.complete_todo(i)

    print("\n6. 查看已完成的待办事项")
    print("-" * 40)
    todos = manager.list_todos(sort_by="id", filter_status="已完成")
    for todo in todos:
        print(f"  {todo}")

    print("\n7. 显示统计信息")
    print("-" * 40)
    stats = manager.get_statistics()
    print(f"总计: {stats['总计']}")
    print(f"已完成: {stats['已完成']}")
    print(f"未完成: {stats['未完成']}")
    print(f"逾期: {stats['逾期']}")

    print("\n8. 删除完成的待办事项")
    print("-" * 40)
    deleted = manager.delete_completed()
    print(f"删除了 {deleted} 个已完成的待办事项")

    print("\n9. 删除后的剩余待办事项")
    print("-" * 40)
    todos = manager.list_todos(sort_by="id", filter_status="全部")
    for todo in todos:
        print(f"  {todo}")

    print("\n10. 最终的统计信息")
    print("-" * 40)
    stats = manager.get_statistics()
    print(f"总计: {stats['总计']}")
    print(f"已完成: {stats['已完成']}")
    print(f"未完成: {stats['未完成']}")

    # 清理演示文件
    if os.path.exists("demo_todos.json"):
        os.remove("demo_todos.json")
        print("\n已清理演示文件: demo_todos.json")

def demo_programmatic_usage():
    """演示编程式使用"""
    print("\n" + "=" * 60)
    print("编程式使用示例")
    print("=" * 60)

    # 创建管理器
    manager = TodoManager("programmatic_todos.json")

    # 清空现有数据
    manager.todos = []
    manager.next_id = 1

    # 使用编程方式添加待办事项
    from todo_manager import TodoItem

    todo1 = TodoItem("编程练习", Priority.HIGH, "2026-06-26", 1)
    todo2 = TodoItem("写文档", Priority.MEDIUM, "2026-06-27", 2)
    todo3 = TodoItem("休息", Priority.LOW, None, 3)

    manager.todos = [todo1, todo2, todo3]
    manager.next_id = 4
    manager.save()

    print("\n添加的待办事项:")
    for todo in manager.todos:
        print(f"  {todo}")

    # 使用各种筛选和排序
    print("\n按截止日期排序:")
    todos = manager.list_todos(sort_by="due_date", filter_status="全部")
    for todo in todos:
        print(f"  {todo}")

    # 清理
    if os.path.exists("programmatic_todos.json"):
        os.remove("programmatic_todos.json")

def demo_api_reference():
    """演示API参考"""
    print("\n" + "=" * 60)
    print("API使用参考")
    print("=" * 60)

    print("""
主要类和方法:

1. TodoManager - 核心管理类
   - add_todo(content, priority, due_date) - 添加待办事项
   - list_todos(sort_by, filter_status) - 列出待办事项
   - complete_todo(todo_id) - 标记为已完成
   - delete_completed() - 删除已完成的
   - delete_todo(todo_id) - 删除特定待办
   - get_statistics() - 获取统计信息
   - save() - 保存数据
   - load() - 加载数据

2. TodoItem - 待办事项类
   - to_dict() - 转换为字典
   - from_dict(data) - 从字典创建
   - complete() - 标记为已完成

3. 枚举类型:
   - Priority: LOW("低"), MEDIUM("中"), HIGH("高"), URGENT("紧急")
   - Status: PENDING("未完成"), COMPLETED("已完成")

4. TodoCLI - 命令行界面
   - run() - 运行CLI程序

使用示例:

    # 创建管理器
    manager = TodoManager("my_todos.json")

    # 添加待办事项
    manager.add_todo("学习Python", "高", "2026-06-30")

    # 查看未完成的待办事项（按优先级排序）
    todos = manager.list_todos(sort_by="priority", filter_status="未完成")

    # 标记为已完成
    manager.complete_todo(1)

    # 获取统计信息
    stats = manager.get_statistics()
    """)

if __name__ == "__main__":
    demo_basic_operations()
    demo_programmatic_usage()
    demo_api_reference()

    print("\n" + "=" * 60)
    print("如何运行:")
    print("=" * 60)
    print("""
1. 运行命令行界面:
   python todo_manager.py

2. 导入使用:
   from todo_manager import TodoManager

   manager = TodoManager()
   manager.add_todo("您的待办事项", "中", "2026-06-25")

3. 运行演示:
   python demo_todo.py
    """)