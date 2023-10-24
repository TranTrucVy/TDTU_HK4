using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _52100674_TranThiVen
{
    public partial class Form1 : Form
    {
        public static string cnStr = System.Configuration.ConfigurationManager.ConnectionStrings["cnStr"].ConnectionString;
        SqlConnection cn = new SqlConnection(cnStr);
        public static int editCode;

        public Form1()
        {
            InitializeComponent();
            editCode = -1;
            radioNam.Checked = true;
        }

        private void loadData()
        {
            cn.Open();

            string query = "SELECT * FROM DOCGIA";
            SqlCommand sqlCommand = new SqlCommand(query, cn);
            SqlDataAdapter da = new SqlDataAdapter(sqlCommand);
            DataSet ds = new DataSet();
            da.Fill(ds, "DOCGIA");
            dataGridView.DataSource = ds.Tables["DOCGIA"].DefaultView;

            cn.Close();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            loadData();

            //dataGridView.Columns[0].HeaderText = "Số điện thoại";
            //dataGridView.Columns[1].HeaderText = "Tài khoản";
            //dataGridView.Columns[2].HeaderText = "Email";
            //dataGridView.Columns[3].HeaderText = "Tên";
            //dataGridView.Columns[4].HeaderText = "Địa chỉ";
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string timKiemDocGia = txtTimKiemDocGia.Text;

            cn.Open();

            string query = "SELECT * FROM DOCGIA WHERE TenDangNhap LIKE CONCAT('%',@timKiemDocGia,'%')";
            SqlCommand sqlCommand = new SqlCommand(query, cn);
            sqlCommand.Parameters.AddWithValue("@timKiemDocGia", timKiemDocGia);
            SqlDataAdapter da = new SqlDataAdapter(sqlCommand);
            DataSet ds = new DataSet();
            da.Fill(ds, "DOCGIA");
            dataGridView.DataSource = ds.Tables["DOCGIA"].DefaultView;

            cn.Close();
        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            txtTenDangNhap.Text = "";
            txtHoTen.Text = "";
            txtNamSinh.Text = "";
            txtDiaChi.Text = "";
            radioNam.Checked = true;
        }

        private void btnSua_Click(object sender, EventArgs e)
        {
            string tenDangNhap = txtTenDangNhap.Text;
            string hoTen = txtHoTen.Text;
            int namSinh = int.Parse(txtNamSinh.Text);
            string diaChi = txtDiaChi.Text;
            bool gioiTinhNam = radioNam.Checked;
            cn.Open();

            string query = "UPDATE DOCGIA " +
                "SET TenDangNhap =@tenDangNhap, HoTen =@hoTen, GioiTinh =@gioiTinhNam, NamSinh =@namSinh, DiaChi =@diaChi "
                + "WHERE MaDocGia = @MaDocGia ";

            SqlCommand cmd = new SqlCommand(query, cn);
            cmd.Parameters.AddWithValue("@MaDocGia", editCode);
            cmd.Parameters.AddWithValue("@tenDangNhap", tenDangNhap);
            cmd.Parameters.AddWithValue("@hoTen", hoTen);
            cmd.Parameters.AddWithValue("@namSinh", namSinh);
            cmd.Parameters.AddWithValue("@diaChi", diaChi);
            cmd.Parameters.AddWithValue("@gioiTinhNam", gioiTinhNam.ToString());

            cmd.ExecuteReader().Close();

            cn.Close();

            loadData();
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void btnThem_Click(object sender, EventArgs e)
        {
            string tenDangNhap = txtTenDangNhap.Text;
            string hoTen = txtHoTen.Text;
            int namSinh = int.Parse(txtNamSinh.Text);
            string diaChi = txtDiaChi.Text;
            bool gioiTinhNam = radioNam.Checked;
            cn.Open();

            string query = "INSERT INTO DOCGIA VALUES "
                + "(@tenDangNhap, @hoTen, @gioiTinhNam, @namSinh, @diaChi)";

            SqlCommand cmd = new SqlCommand(query, cn);
            cmd.Parameters.AddWithValue("@tenDangNhap", tenDangNhap);
            cmd.Parameters.AddWithValue("@hoTen", hoTen);
            cmd.Parameters.AddWithValue("@namSinh", namSinh);
            cmd.Parameters.AddWithValue("@diaChi", diaChi);
            cmd.Parameters.AddWithValue("@gioiTinhNam", gioiTinhNam.ToString());

            cmd.ExecuteReader().Close();

            cn.Close();

            loadData();
        }

        private void txtMaDocGia_TextChanged(object sender, EventArgs e)
        {

        }

        private void radioButton1_CheckedChanged_1(object sender, EventArgs e)
        {

        }

        private void dataGridView_CellDoubleClick(object sender, DataGridViewCellEventArgs e)
        {
            editCode = int.Parse(dataGridView.CurrentRow.Cells[0].Value.ToString());
            txtTenDangNhap.Text = dataGridView.CurrentRow.Cells[1].Value.ToString();
            txtHoTen.Text = dataGridView.CurrentRow.Cells[2].Value.ToString();
            if ((bool)dataGridView.CurrentRow.Cells[3].Value)
            {
                radioNam.Checked = true;
            }
            else
            {
                radioNu.Checked = true;
            }
            txtNamSinh.Text = dataGridView.CurrentRow.Cells[4].Value.ToString();
            txtDiaChi.Text = dataGridView.CurrentRow.Cells[5].Value.ToString();
        }

        private void btnXoa_Click(object sender, EventArgs e)
        {
            int code = int.Parse(dataGridView.CurrentRow.Cells[0].Value.ToString());

            if (code == editCode)
            {
                MessageBox.Show("Hãy hủy chỉnh sửa trước khi xóa!");
                return;
            }

            SqlCommand cmd;
            cn.Open();

            string query1 =
                "SELECT * FROM PHIEUMUON " +
                "WHERE MaDocGia = @MaDocGia";
            cmd = new SqlCommand(query1, cn);
            cmd.Parameters.AddWithValue("@MaDocGia", code);
            SqlDataReader r = cmd.ExecuteReader();

            if (r.Read())
            {
                MessageBox.Show("Doc gia da co muon sach");
                cn.Close();
                return;
            }
            r.Close();

            string query2 =
                "SELECT * FROM PHIEUTRA " +
                "WHERE MaDocGia= @MaDocGia";
            cmd = new SqlCommand(query2, cn);
            cmd.Parameters.AddWithValue("@MaDocGia", code);
            SqlDataReader r1 = cmd.ExecuteReader();

            if (r1.Read())
            {
                MessageBox.Show("Doc gia da co tra sach");
                cn.Close();
                return;
            }
            r1.Close();

            string query3 =
                "DELETE FROM DOCGIA " +
                "WHERE MaDocGia = @MaDocGia";
            cmd = new SqlCommand(query3, cn);
            cmd.Parameters.AddWithValue("@MaDocGia", code);
            cmd.ExecuteReader().Close();

            cn.Close();

            loadData();
        }

        private void dataGridView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }
    }
}
