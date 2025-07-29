"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход путь до файла с логами
    и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, хранящиеся в бинарном дереве уникальны
"""

import itertools
import logging
import random
from collections import deque
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int
    left: Optional["BinaryTreeNode"] = None
    right: Optional["BinaryTreeNode"] = None

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10**6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node


def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    nodes = {}
    children_map = {}
    visiting_order = []

    with open(path_to_log_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "Visiting" in line:
                # Извлекаем значение узла
                val = int(line.split("[")[1].split("]")[0])
                visiting_order.append(val)
                if val not in nodes:
                    nodes[val] = BinaryTreeNode(val)
            elif "left is not empty" in line or "right is not empty" in line:
                parts = line.split("<BinaryTreeNode[")
                parent_val = int(parts[1].split("]")[0])
                child_val = int(parts[2].split("]")[0])

                if parent_val not in nodes:
                    nodes[parent_val] = BinaryTreeNode(parent_val)
                if child_val not in nodes:
                    nodes[child_val] = BinaryTreeNode(child_val)

                if parent_val not in children_map:
                    children_map[parent_val] = [None, None]

                if "left" in line:
                    children_map[parent_val][0] = child_val
                else:
                    children_map[parent_val][1] = child_val

    # Восстанавливаем связи
    for parent_val, (left_val, right_val) in children_map.items():
        parent = nodes[parent_val]
        if left_val:
            parent.left = nodes[left_val]
        if right_val:
            parent.right = nodes[right_val]

    # Корень — это первый посещённый узел
    root_val = visiting_order[0]
    return nodes[root_val]


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename="walk_log_4.txt",
    )

    root = get_tree(7)
    walk(root)
    print(restore_tree("walk_log_4.txt"))
