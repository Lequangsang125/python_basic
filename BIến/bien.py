# là nơi chứa dữ liệu
# python không có lệnh để khai báo
# đc tạo ra khi gán giá trị cho nó
# biến không cần khai báo kiểu dữ liệu và có thể gán lại kiểu dữ liệu
# tên biến phân biệt chữ hoa và thường
x = 4
x = 'hello'
print(x)

#Ép kiểu
x = str(3)
print(x)
y = int(3)
print(y)
z = float(3)
print(z)

# kiểm tra kiểu dữ liệu 
print(type(x))
print(type(y))
print(type(z))

### Tên biến
# Tên biến phải bắt đầu chữ cái hoặc ký tự gạch dưới
# Tên biến không thể bắt đầu bằng số
# Tên biến phân biệt chữ hoa và thường

# Biến python - gán nhiều giá trị
x, y, z = "Orange","Banana","Cherry"
print(x)
print(y)
print(z)

# Gán 1 giá trị cho nhiều biến 
x = y = z = 'orange'
print(x)
print(y)
print(z)

# Giải nén trong python
x = 'l'
y = 'q'
z = 's'
print(x,y,z)
print(x + y + z)

print('hello', 'world')

# biến toàn cục là các biến tạo bên ngoài hàm
# sử dụng đc cả bên trong và ngoài hàm
x = 'lesang'
def myFunc():
    x = 'Aki'
    print("Toi la" + x)
myFunc()
print("Toi la" + x)

# muốn tạo biến toàn cục trong hàm thì dùng global
def myFunc1():
    global x 
    x = 'lesang'
    print('taola ' + x)
myFunc1()
print('taolas ' + x)