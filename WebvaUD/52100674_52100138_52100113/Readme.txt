Springcommerce là một web bán hàng được xây dựng trên nền tảng Spring Framework và sử dụng MySQL làm cơ sở dữ liệu. 
Springcommerce cung cấp các chức năng cơ bản để người dùng có thể thêm sản phẩm vào giỏ hàng, thanh toán,login.

Các chức năng chính
Hiển thị sản phẩm: Người dùng có thể xem danh sách sản phẩm và chi tiết từng sản phẩm.
Thêm sản phẩm vào giỏ hàng: Người dùng có thể thêm sản phẩm vào giỏ hàng và chỉnh sửa số lượng sản phẩm trong giỏ hàng.
Thanh toán: Người dùng có thể thanh toán đơn hàng và nhập thông tin liên lạc và địa chỉ giao hàng.  

Cài đặt
Để chạy Springcommerce, bạn cần cài đặt các phần mềm sau:
JDK 17 trở lên
MySQL
MySQL Workbench
Gradle groovy

Sau khi cài đặt các phần mềm trên, bạn có thể sử dụng lệnh sau để chạy ứng dụng:
Cấu trúc thư mục
src/main/java: Chứa các class Java.
src/main/resources: Chứa các file cấu hình cho ứng dụng.
src/test: Chứa các test case cho ứng dụng.
Các thư viện sử dụng
Springcommerce sử dụng các thư viện sau:

SpringBoot Framework
MySQL Connector
Thymeleaf
Bootstrap 5
MDBootstrap

Em có để file sql thiết kế database trong package: com.tdtu.javatech.SpringCommerce.config.db và cả ở ngoài thư mục source

Bước 1: Dùng file sql database để chạy trong mysql 
Bước 2: Config ở 2 file application.properties, generatorMyBatis.xml về password cũng như root mà bạn đã settings ở mysql
Bước 3: Khởi chạy file build.gradle để cài dependencies 
Bước 4: Dùng file SpringCommerceApplication.java run as với Spring Boot

