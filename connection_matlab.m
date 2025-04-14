% เชื่อมต่อกับ TCP server ที่ Python เปิดอยู่
clc;
t = tcpclient('127.0.0.1', 9999);

disp("เชื่อมต่อกับ Python เรียบร้อย");

while true
    if t.NumBytesAvailable > 0
        data = read(t, t.NumBytesAvailable, "string");
        disp("ข้อมูลที่ได้รับจาก Python: " + data);
    end
    pause(0.1); 
end
