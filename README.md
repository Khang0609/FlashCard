# FlashCard

LƯU Ý

Thư mục .vscode chứa file launch.json không liên quan đến tính năng của phần mềm, nó dùng để setting cho VS sẽ auto debug file interface.py khi ấn phím F5.
Tuy nhiên nếu bạn muốn cài đặt về như cũ, sửa dòng 11 trong file launch.json "program": "interface.py", thành "program": "${file}", là được.
----------------------------------------------------------
HƯỚNG DẪN SỬ DỤNG TRƯỚC KHI DÙNG

Để có thể tùy chỉnh những từ cần học, các bạn vào file tu_vung.txt trong folder file và thêm từ theo cú pháp
       
            từ vựng tiếng anh:nghĩa tiếng việt

        ví dụ: hello:xin chao, apple:tao,...

Nhưng nếu bạn muốn thêm file từ vụng mới, mình cũng sẽ tạo file .txt ở trong folder file và thêm từ như trên. Tuy nhiên các bạn cần vào file path, đổi tên đường dẫn cho biến VOCABULARY, ban đầu là VOCABULARY = "file/tu_vung.txt", và các bạn có thể đổi thành VOCABULARY = "file/academic.txt" ví dụ vậy.