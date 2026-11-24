import torch
import json

def validate_record(record):
    # record是传入值，要判断传入值的几个错误：
    # 1.判断reccord是否是字典类型
    # 2. 判断record 是否包含id，text两个key
    #3. 判断record 的，id，text是不是string类型
    # 4. 判断record的id，text是否为空：
    if not isinstance(record,dict):
        raise ValueError(f"Record must be a dict,but got {type(record)}")
   # 如果是dict
    for field in ("id","text"):
        if field not in record:
            raise ValueError(f"record must contain '{field}' field,but not found")
            if not isinstance(record[field],str):
                raise ValueError(f"{field} must be a string")
            if not record[field].strip():
                raise ValueError(f"{field} must not be empty or whitspace")

def read_jsonl(path) -> list[dict]:#测试文件路径的
    records = []
    with open(path,"r",encoding="utf-8") as file:
        for line_num, line in enumerate(file,start=1):
            line = line.strip()

            if not line:
                continue
            try:
                record = json.loads(line)
                validate_record(record)
            except ValueError as e:
                raise ValueError(f"Invalid record at line {line_num}: {e}")
            records.append(record)
        return records




def write_jsonl(path, records) -> None:
    # path：要写入的文件路径
    # records：需要写入文件的字典列表
    # -> None：表示函数不需要返回结果

    # 创建空列表，用来存放序列化后的 JSON 字符串
    lines = []

    # 遍历 records 中的每一条记录
    # record_num：当前是第几条记录，从 1 开始
    # record：当前取出的字典
    for record_num, record in enumerate(records, start=1):

        try:
            # 调用之前写好的函数，检查当前记录是否合法
            validate_record(record)

            # 将 Python 字典转换为 JSON 字符串
            # ensure_ascii=False：保留中文等非 ASCII 字符
            line = json.dumps(record, ensure_ascii=False)

        except (ValueError, TypeError) as exc:

            # 如果校验或序列化失败，抛出异常
            # 同时说明第几条记录出现了错误
            raise ValueError(
                f"{path}: record {record_num}: {exc}"
            ) from exc

        # 将序列化后的字符串添加到列表中
        # \n 表示换行，保证每条记录独占一行
        lines.append(line + "\n")

    # 注意：这里已经完成了所有记录的校验和序列化
    # 确认所有记录都合法后，才打开文件

    # "w" 表示写入模式
    # 如果文件不存在，就创建文件
    # 如果文件已经存在，就清空原来的内容
    with open(path, "w", encoding="utf-8") as file:

        # 将 lines 列表中的所有字符串依次写入文件
        file.writelines(lines)







