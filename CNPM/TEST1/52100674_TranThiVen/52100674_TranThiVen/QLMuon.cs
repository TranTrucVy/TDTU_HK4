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

namespace _52100674_TranThiVen
{
    public partial class QLMuon : Form
    {
        public static string cnStr = System.Configuration.ConfigurationManager.ConnectionStrings["cnStr"].ConnectionString;
        SqlConnection cn = new SqlConnection(cnStr);
        public static int editCode;
        public QLMuon()
        {
            InitializeComponent();
            editCode = -1;
        }
        private void loadData()
        {
            cn.Open();

            string query = "SELECT * FROM PHIEUMUON";
            SqlCommand sqlCommand = new SqlCommand(query, cn);
            SqlDataAdapter da = new SqlDataAdapter(sqlCommand);
            DataSet ds = new DataSet();
            da.Fill(ds, "PHIEUMUON");
            dataGridView.DataSource = ds.Tables["PHIEUMUON"].DefaultView;

            cn.Close();
        }
       
        private void label7_Click(object sender, EventArgs e)
        {
            label7.Font = new Font(label7.Font, FontStyle.Bold);
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void btnThem_Click(object sender, EventArgs e)
        {

        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void QLMuon_Load(object sender, EventArgs e)
        {
                loadData();

                //dataGridView.Columns[0].HeaderText = "Số điện thoại";
                //dataGridView.Columns[1].HeaderText = "Tài khoản";
                //dataGridView.Columns[2].HeaderText = "Email";
                //dataGridView.Columns[3].HeaderText = "Tên";
                //dataGridView.Columns[4].HeaderText = "Địa chỉ";

        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            txtTenDangNhap.Text = "";
            txtHoTen.Text = "";
            txtTimKiemSach.Text = "";
        }

        private void dataGridView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
