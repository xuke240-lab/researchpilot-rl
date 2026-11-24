import pytest
from src.data.jsonl_io import validate_record,read_jsonl,write_jsonl

def test_validate_record():
    record = {
        "id": "123",
        "text": "This is a test record."
    }
    validate_record(record)

def test_validate_record_missing_field():
    record = {
        "id": "123"
    }
    with pytest.raises(ValueError):
        validate_record(record)

def test_validate_record_jsonl(tmp_path):
    path = tmp_path / "test.jsonl"
    path.write_text(
    '{"id": "001", "text": "Hello"}\n'
    '\n'
    '{"id": "002"}\n',
    encoding="utf-8")
    with pytest.raises(ValueError):
        read_jsonl(path)
    

import pytest

# 导入我们目前编写的三个函数
from src.data.jsonl_io import (
    validate_record,
    read_jsonl,
    write_jsonl
)


def test_write_jsonl(tmp_path):

    # pytest 自动创建临时文件夹
    # 拼接出需要写入的文件路径
    # 此时文件还没有被创建
    path = tmp_path / "test.jsonl"

    # 准备需要写入的原始数据
    records = [
        {"id": "001", "text": "你好"},
        {"id": "002", "text": "Python"}
    ]

    # 调用 write_jsonl 创建文件并写入记录
    write_jsonl(path, records)

    # 检查文件是否成功创建
    assert path.exists()

    # 调用之前写好的 read_jsonl 读取文件
    result = read_jsonl(path)

    # 检查读取出来的数据是否与原始数据完全一致
    assert result == records

    # 检查文件中的中文是否被直接保留
    assert "你好" in path.read_text(encoding="utf-8")


def test_write_jsonl_invalid_record(tmp_path):

    # 创建临时文件路径
    path = tmp_path / "test.jsonl"

    # 提前创建一个文件，模拟已经存在的数据
    original = '{"id": "000", "text": "Original"}\n'
    path.write_text(original, encoding="utf-8")

    # 第一条记录合法
    # 第二条记录缺少 text 字段，不合法
    records = [
        {"id": "001", "text": "Hello"},
        {"id": "002"}
    ]

    # 预期 write_jsonl 抛出 ValueError
    # match 用于检查错误信息中是否包含 record 2
    with pytest.raises(ValueError, match="record 2"):
        write_jsonl(path, records)

    # 读取原文件，检查内容是否发生改变
    # 如果仍然等于 original，说明原有数据没有被破坏
    assert path.read_text(encoding="utf-8") == original

