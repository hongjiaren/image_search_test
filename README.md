# 图片采集工具

本项目是一个高质量图片采集工具，参考 deerflow 框架的搜图能力，支持通过关键词批量采集网络图片，自动去重（基于 imagehash），并按规范重命名和保存图片。

## 功能特性
- 支持通过关键词采集高质量图片
- 保持原图片格式（jpg、png、webp等）
- 自动去重，避免重复图片（imagehash）
- 图片重命名，便于管理
- 命令行参数灵活配置

## 环境依赖
- Python 3.8+
- 依赖包见 requirements.txt

## 安装依赖
```bash
pip install -r requirements.txt
```

## 使用方法
```bash
python main.py --query "猫" --output_dir ./images --max_count 20
```
参数说明：
- `--query`：图片搜索关键词
- `--output_dir`：图片保存目录
- `--max_count`：最多采集图片数量（可选，默认20）

## 目录结构
```
image-crawler/
  README.md
  requirements.txt
  .gitignore
  main.py
  src/
    __init__.py
    ...
```

## 参考
- [deerflow](https://github.com/bytedance/deer-flow)
- [PEP 8](https://peps.python.org/pep-0008/)
- [PEP 484](https://peps.python.org/pep-0484/)
- [PEP 526](https://peps.python.org/pep-0526/)
