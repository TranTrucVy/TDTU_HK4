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
    public partial class QLTraSach : Form
    {
        public static string cnStr = System.Configuration.ConfigurationManager.ConnectionStrings["cnStr"].ConnectionString;
        SqlConnection cn = new SqlConnection(cnStr);
        public static int editCode;
        public QLTraSach()
        {
            InitializeComponent();
            editCode = -1;
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
        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void QLTraSach_Load(object sender, EventArgs e)
        {
            loadData();

        }

        private void btnClear_Click(object sender, EventArgs e)
        {
            txtTenDangNhap.Text = "";
            txtHoTen.Text = "";
            txtTimKiemLichTra.Text = "";
        }
    }
}
