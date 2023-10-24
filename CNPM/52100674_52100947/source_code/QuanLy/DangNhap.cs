using QuanLy.Class;
using System;
using System.Windows.Forms;

namespace QuanLy
{
    public partial class DangNhap : Form
    {
        public DangNhap()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            TaiKhoan tk = new TaiKhoan();
            int m = tk.DangNhap(tdn.Text, mk.Text);
            if (m != -1)
            {
                Session.taikhoan = tdn.Text;
                if (m == 1)
                {
                    Admin ad = new Admin();
                    this.Hide();
                    ad.ShowDialog();
                    this.Close();
                }
                else
                {
                    Users ad = new Users();
                    this.Hide();
                    ad.ShowDialog();
                    this.Close();
                }
            }
            else
            {
                MessageBox.Show("Sai tài khoản mật khẩu");
            }

        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            DangKi dk = new DangKi();

            this.Hide();
            dk.ShowDialog();
            this.Close();
        }

    }
}
