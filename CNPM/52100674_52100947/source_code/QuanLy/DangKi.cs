using QuanLy.Class;
using System;
using System.Windows.Forms;

namespace QuanLy
{
    public partial class DangKi : Form
    {
        public DangKi()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DangNhap dn = new DangNhap();
            this.Hide();
            dn.ShowDialog();
            this.Close();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            TaiKhoan tk = new TaiKhoan();
            if (mk.Text.Length < 6)
            {
                MessageBox.Show("Mật khẩu tối thiểu 6 kí tự.");
            }
            if (sdt.Text.Length > 10 && sdt.Text.Length <10)
            {
                MessageBox.Show("Số điện thoại không đúng kiểu.");

            }
            else
            {
                try
                {
                    int m = tk.CheckTK(tdn.Text);
                    if (m == -1)
                    {
                        tk.DangKi(tdn.Text, mk.Text,sdt.Text,email.Text);
                        MessageBox.Show("Đăng kí thành công.");
                        DangNhap dn = new DangNhap();
                        this.Hide();
                        dn.ShowDialog();
                        this.Close();
                    }
                    else
                    {
                        MessageBox.Show("Tên đăng nhập đã tồn tại.");
                    }

                }
                catch (Exception ex)
                {
                    MessageBox.Show("Dữ liệu lỗi");
                }
            }

        }

    }
}
