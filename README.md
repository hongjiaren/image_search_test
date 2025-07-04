# 图片采集工具（Tavily 高质量图片爬取）

## 项目简介

本项目是一个基于 Tavily API 的高质量图片采集工具，支持命令行一键采集指定关键词的图片，自动去重、重命名、保留原格式，并支持图片描述信息保存。适合数据集采集、AI 训练、报告插图等多种场景。

## 主要特性

- 支持 Tavily 搜图 API，采集高质量图片
- 命令行参数灵活，支持关键词、保存目录、图片数量自定义
- 自动去重（感知哈希 imagehash）
- 图片重命名，便于管理
- 保留原始图片格式（jpg/png/gif/webp等）
- 每张图片可保存描述信息（如有）
- 详细日志提示，易于调试和扩展

## 目录结构

```
image-crawler/
│
├── main.py                  # 项目主入口，只负责参数解析和主流程调用
├── requirements.txt         # 依赖包列表
├── .env                     # API Key等环境变量（需自行创建）
├── README.md                # 项目说明文档
│
└── src/
    ├── __init__.py
    ├── search_image.py      # Tavily 搜图API封装
    └── download_images.py   # 图片下载、去重、重命名

```

## 环境依赖

- Python 3.10.18
- 依赖包见 requirements.txt

安装依赖：

```bash
pip install -r requirements.txt
```

## API Key 配置

1. 在项目根目录下创建 `.env` 文件，内容如下：

   ```
   TAVILY_API_KEY=你的_tavily_api_key
   ```

2. 你可以在 [Tavily 官网](https://app.tavily.com/) 注册并获取 API Key。

## 使用方法

### 命令行采集图片

```bash
python main.py --query "中国" --save_dir ./output --max_results 4
```

参数说明：

- `--query`：图片搜索关键词（必填）
- `--save_dir`：图片保存目录（可选，默认 images）
- `--max_results`：最多采集图片数量（可选，默认 5）

### 运行示例

```bash
python main.py --query "长城" --save_dir ./output --max_results 3
```

输出示例：

```
即将下载 3 张图片，保存到目录: ./output
[1] 正在下载: https://xxx.jpg
[1] 已保存: ./output/image_001.jpg（格式: jpg）
...
下载完成，成功保存图片数量: 3
```

## 代码风格与规范

- 遵循 [PEP8](https://peps.python.org/pep-0008/) 代码风格
- 类型注解 [PEP484](https://peps.python.org/pep-0484/)
- 变量命名清晰，结构合理，易于维护

## 常见问题

- **图片数量少于 max_results？**  
  可能是关键词下 Tavily API 可用图片有限，或 API 限制。终端会有友好提示。

- **403/下载失败？**  
  已自动加 User-Agent，大部分站点可正常下载。个别站点如有反爬限制，建议更换关键词或图片源。

## 贡献与反馈

欢迎提交 issue 或 PR 进行改进和交流！ 