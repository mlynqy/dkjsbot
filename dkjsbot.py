import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# 启用日志方便调试
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# 计算端口的函数
def calculate_ports(n, ssh_base=10000, service_base=20000, range_size=10):
    ssh_port = ssh_base + n
    service_start = service_base + (n) * range_size
    service_end = service_start + range_size - 1
    return ssh_port, service_start, service_end

# 处理 /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("欢迎使用端口号计算器！\n请输入一个尾号 n（例如 38）。")

# 处理用户输入数字
async def handle_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        n = int(update.message.text.strip())
        ssh_port, service_start, service_end = calculate_ports(n)
        # 转义特殊字符（如 -）
        reply = (
            f"尾号 {n} 的计算结果：\n"
            f"SSH端口：`{ssh_port}`\n"
            f"开放端口：`{service_start}` \\- `{service_end}`"  # 注意转义了 -
        )
    except ValueError:
        reply = "请输入一个正确的数字！"
    
    # 发送带有 MarkdownV2 格式的消息
    await update.message.reply_text(reply, parse_mode="MarkdownV2")

def main():
    # 替换成你的 Bot Token
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_number))

    print("Bot 已启动...")
    app.run_polling()

if __name__ == "__main__":
    main()

