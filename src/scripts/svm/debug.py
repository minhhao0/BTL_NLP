import pandas as pd

# Đọc file CSV
file_path = "comment.csv"   # thay bằng đường dẫn file thật
df = pd.read_csv(file_path)

# Đặt tên cột nếu file chỉ có 1 cột
df.columns = ["comment"]

# Danh sách từ khóa cần loại bỏ
keywords = ["Chào anh", "Thân mến", "Bên em", "giá chỉ", "Chào chị", "Dạ tủ lạnh","đ"]

# Lọc dữ liệu: giữ lại các dòng KHÔNG chứa các từ khóa (không phân biệt hoa thường)
mask = ~df["comment"].str.lower().str.contains("|".join(k.lower() for k in keywords), na=False)
filtered_df = df[mask].copy()

# Thêm cột số thứ tự ở bên trái (bắt đầu từ 1)
filtered_df.insert(0, "index", range(1, len(filtered_df) + 1))

# Xuất ra file mới
filtered_df.to_csv("comment_filtered.csv", index=False, encoding="utf-8-sig")

print("Đã lọc xong, kết quả lưu vào 'comment_filtered.csv'")
