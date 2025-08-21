from pathlib import Path
import json


def sums(file_path: str, field_name: str) -> int:
    """统计JSON数组中所有的总和"""
    path = Path(file_path)

    # 检查文件存在性和可读性
    path.resolve(strict=True)

    # 读取并解析JSON
    data = json.loads(path.read_text(encoding='utf-8'))
    l = list(data)
    # l = [p for p in data if p["curr_hour"] == 12]
    # print(len(l))

    # 验证数据类型
    if not isinstance(l, list):
        raise ValueError("JSON数据不是数组")

    # 使用生成器表达式和内置函数求和
    return sum(
        float(item[field_name]) if item[field_name] != '' else 0
        for item in l
        if isinstance(item, dict) and field_name in item
    )


if __name__ == "__main__":
    path = r"D:\test.json"
    field = 'member_countas'

    al = [field]
    res = list()
    try:
        for i, e in enumerate(al):
            result = sums(path, e)
            print(f"总和: {result}")
            res.append(result)
    except Exception as e:
        print(f"错误: {e}")

    print(res)
    # path = r"D:\test.json"
    # # field = 'avg_stay'
    # field = 'distinct_count'
    # try:
    #     result = sums(path, field)
    #     print(f"总和: {result}")
    # except Exception as e:
    #     print(f"错误: {e}")
