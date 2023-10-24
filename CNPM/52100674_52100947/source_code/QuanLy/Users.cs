using Microsoft.Office.Interop.Excel;
using QuanLy.Class;
using Quanlysanbong;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace QuanLy
{
    public partial class Users : Form
    {
        public Users()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {
            DangNhap dn = new DangNhap();
            this.Hide();
            dn.ShowDialog();
            this.Close();
        }
        public void hienthicbxmg()
        {
            ketnoi k = new ketnoi();
            SqlConnection con = k.GetConnection();
            string sql2 = "select * from MuaGiai ";
            System.Data.DataTable tb2 = new System.Data.DataTable();
            SqlDataAdapter ad2 = new SqlDataAdapter(sql2, con);
            ad2.Fill(tb2);
            cbxcmg.DataSource = tb2;
            cbxcmg.DisplayMember = "TenMuaGiai";
            cbxcmg.ValueMember = "Id";
        }
        public void hienthicbxltd()
        {
            ketnoi k = new ketnoi();
            SqlConnection con = k.GetConnection();
            string sql2 = "select * from MuaGiai ";
            System.Data.DataTable tb2 = new System.Data.DataTable();
            SqlDataAdapter ad2 = new SqlDataAdapter(sql2, con);
            ad2.Fill(tb2);
            cbxltd.DataSource = tb2;
            cbxltd.DisplayMember = "TenMuaGiai";
            cbxltd.ValueMember = "Id";
        }
        public void hienthicbxclb()
        {
            ketnoi k = new ketnoi();
            SqlConnection con = k.GetConnection();
            string sql2 = "select * from CauLacBo ";
            System.Data.DataTable tb2 = new System.Data.DataTable();
            SqlDataAdapter ad2 = new SqlDataAdapter(sql2, con);
            ad2.Fill(tb2);
            cbxclb.DataSource = tb2;
            cbxclb.DisplayMember = "TenCLB";
            cbxclb.ValueMember = "Id";
        }
        public void hienthimg()
        {
            XepHang xh = new XepHang();
            System.Data.DataTable h = xh.DanhSach(int.Parse(cbxcmg.SelectedValue.ToString()));
            tablekq.DataSource = h;
            for (int i = 0; i < tablekq.Columns.Count; i++)
            {
                this.tablekq.Columns[i].AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
            }
        }
        public void hienthiclb()
        {
            CauLacBo clb1=new CauLacBo();
            System.Data.DataTable h = clb1.DanhSach();
            tableclb.DataSource = h;
            for (int i = 0; i < tableclb.Columns.Count; i++)
            {
                this.tableclb.Columns[i].AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
            }
        }
        private void Users_Load(object sender, EventArgs e)
        {
            hienthicbxmg();
            hienthicbxltd();
            hienthicbxclb();
            hienthiclb();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            XepHang xh = new XepHang();
            ExportToExcel obj = new ExportToExcel();
            System.Data.DataTable dt = xh.DanhSach(int.Parse(cbxcmg.SelectedValue.ToString()));
            tablekq.DataSource = dt;
            SaveFileDialog s = new SaveFileDialog();
            if (s.ShowDialog() == DialogResult.OK && tablekq.RowCount > 0)
            {
                bool export = obj.ToExcel(dt, s.FileName, "Bảng xếp hạng " + cbxcmg.Text, dt.Columns.Count);
                MessageBox.Show("Xuất file thành công");
            }
        }

        private void button29_Click(object sender, EventArgs e)
        {
            textmg.Text = "Danh sách kết quả mùa giải " + cbxcmg.Text;
            hienthimg();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            LichThiDau xh = new LichThiDau();
            System.Data.DataTable h = xh.LTD(int.Parse(cbxltd.SelectedValue.ToString()));
            ltd.DataSource = h;
            for (int i = 0; i < ltd.Columns.Count; i++)
            {
                this.ltd.Columns[i].AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            CauThu xh = new CauThu();
            System.Data.DataTable h = xh.CLB(int.Parse(cbxclb.SelectedValue.ToString()));
            tbclb.DataSource = h;
            for (int i = 0; i < tbclb.Columns.Count; i++)
            {
                this.tbclb.Columns[i].AutoSizeMode = DataGridViewAutoSizeColumnMode.Fill;
            }
        }

        private void tabControl1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (((TabControl)sender).SelectedTab == tabPage5)
            {
                Session.taikhoan = null;
                DangNhap dn = new DangNhap();
                this.Hide();
                dn.ShowDialog();
                this.Close();
            }
        }

        private void btn_ChangePass_Click(object sender, EventArgs e)
        {
            TaiKhoan tk = new TaiKhoan();
            int m = tk.DangNhap(Session.taikhoan, txtbPass.Text);
            if (m != -1)
            {
                if (txtbRe_Pass.Text == txtbxNewPass.Text)
                {
                    ketnoi kn = new ketnoi();
                    SqlConnection con = kn.GetConnection();
                    string pass = txtbxNewPass.Text;
                    string sql1 = "UPDATE TaiKhoan SET MatKhau='" + pass + "' WHERE TenDangNhap = '" + Session.taikhoan + "'";
                    con.Open();
                    SqlCommand cmd1 = new SqlCommand(sql1, con);
                    SqlDataReader rd1 = cmd1.ExecuteReader();

                    MessageBox.Show("Đổi mật thành công");
                }
                else
                {
                    MessageBox.Show("Không trùng khớp mật khẩu");
                }
            }
        }
    }
}
