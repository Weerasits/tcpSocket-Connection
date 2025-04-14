import socket

# สร้าง TCP Server
HOST = '127.0.0.1'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("🟢 รอการเชื่อมต่อจาก MATLAB...")

conn, addr = server.accept()
print(f"🔗 เชื่อมต่อกับ: {addr}")

try:
    while True:
        # รับข้อมูลจากผู้ใช้
        message = input("พิมพ์ข้อความที่จะส่งไปให้ MATLAB (พิมพ์ 'exit' เพื่อออก): ")

        if message.lower() == 'exit':
            print("🛑 ปิดการเชื่อมต่อ")
            break

        # ส่งข้อมูลไปให้ MATLAB
        conn.sendall(message.encode())
        print(f"📤 ส่งข้อมูล: {message}")

except KeyboardInterrupt:
    print("\n🛑 หยุดด้วย Ctrl+C")

conn.close()
server.close()
