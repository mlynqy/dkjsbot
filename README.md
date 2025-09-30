# dkjsbot
用于计算nat的端口（适用于无忧云模板类型的）

启用之后，仅需start一下

发送内网ip尾数即可开始计算

类如 10.0.1.38

发送38

bot回复：

尾号 38 的计算结果：

SSH端口：10038

开放端口：20380 - 20389


我以无忧云的nat为例的，只计算了开放的10个端口

如果你是其他类似模板有更多数量或少数端口的，仅需改动range_size值

ssh和开放的base值也可以改为你实际提供商的范围


python依赖： pip install python-telegram-bot
