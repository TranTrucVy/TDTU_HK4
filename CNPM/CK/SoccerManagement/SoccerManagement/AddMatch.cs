using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SoccerManagement
{
    public partial class AddMatch : Form
    {
        public AddMatch()
        {
            InitializeComponent();
        }
        public void LoadMatchs()
        {
            using (SqlConnection connection = new SqlConnection(@"Data Source=.;Initial Catalog=QLDB;Integrated Security=True"))
            {

                connection.Open();
                string query = "Select IDMatch, T1.PIC,T1.CLBNAME,T2.PIC,T2.CLBNAME, DATE,TIME, STAYDIUM,R.REF_NAME from CLUB as T1, CLUB as T2, MATCH1 as M,REFEREE as R where M.CLB1 = T1.IDCLB and " +
                    "M.CLB2 = T2.IDCLB and M.IDREF = R.IDREF";

                SqlDataAdapter ada = new SqlDataAdapter(query, connection);
                DataTable dt = new DataTable();
                ada.Fill(dt);

                DataGridView_match.DataSource = dt;

                DataGridView_match.Columns[0].HeaderText = "ID";
                DataGridView_match.Columns[1].HeaderText = "";
                DataGridView_match.Columns[2].HeaderText = "Host team";
                DataGridView_match.Columns[3].HeaderText = "";
                DataGridView_match.Columns[4].HeaderText = "Visit team";
                DataGridView_match.Columns[5].HeaderText = "Date";
                DataGridView_match.Columns[6].HeaderText = "Time";
                DataGridView_match.Columns[7].HeaderText = "Stadium";
                DataGridView_match.Columns[8].HeaderText = "REF";

                DataGridViewImageColumn imageColumn = new DataGridViewImageColumn();
                imageColumn = (DataGridViewImageColumn)DataGridView_match.Columns[1];
                imageColumn.ImageLayout = DataGridViewImageCellLayout.Zoom;

                DataGridViewImageColumn imageColumn1 = new DataGridViewImageColumn();
                imageColumn1 = (DataGridViewImageColumn)DataGridView_match.Columns[3];
                imageColumn1.ImageLayout = DataGridViewImageCellLayout.Zoom;

                DataGridView_match.Columns[5].DefaultCellStyle.Format = "dd/MM/yyyy";
                DataGridView_match.Columns[6].DefaultCellStyle.Format = @"hh\:mm";

                DataGridView_match.Columns[0].Width = 70;
                DataGridView_match.Columns[1].Width = 40;
                DataGridView_match.Columns[2].Width = 140;
                DataGridView_match.Columns[3].Width = 40;
                DataGridView_match.Columns[4].Width = 140;
                DataGridView_match.Columns[5].Width = 100;
                DataGridView_match.Columns[6].Width = 70;
                DataGridView_match.Columns[7].Width = 90;
                DataGridView_match.Columns[8].Width = 110;

                connection.Close();
            }
        }
        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            using (SqlConnection connection = new SqlConnection(@"Data Source=.;Initial Catalog=QLDB;Integrated Security=True"))
            {
                connection.Open();
                string query = "Select IDMatch, T1.PIC,T1.CLBNAME,T2.PIC,T2.CLBNAME, DATE,TIME, STAYDIUM,R.REF_NAME from CLUB as T1, CLUB as T2, MATCH1 as M,REFEREE as R where M.CLB1 = T1.IDCLB and " +
                    "M.CLB2 = T2.IDCLB and M.IDREF = R.IDREF and DATE = '" + dateTimePicker1.Value + "'";

                SqlDataAdapter ada = new SqlDataAdapter(query, connection);
                DataTable dt = new DataTable();
                ada.Fill(dt);

                DataGridView_match.DataSource = dt;

                DataGridView_match.Columns[0].HeaderText = "ID";
                DataGridView_match.Columns[1].HeaderText = "";
                DataGridView_match.Columns[2].HeaderText = "Host team";
                DataGridView_match.Columns[3].HeaderText = "";
                DataGridView_match.Columns[4].HeaderText = "Visit team";
                DataGridView_match.Columns[5].HeaderText = "Date";
                DataGridView_match.Columns[6].HeaderText = "Time";
                DataGridView_match.Columns[7].HeaderText = "Stadium";
                DataGridView_match.Columns[8].HeaderText = "REF";

                DataGridViewImageColumn imageColumn = new DataGridViewImageColumn();
                imageColumn = (DataGridViewImageColumn)DataGridView_match.Columns[1];
                imageColumn.ImageLayout = DataGridViewImageCellLayout.Zoom;

                DataGridViewImageColumn imageColumn1 = new DataGridViewImageColumn();
                imageColumn1 = (DataGridViewImageColumn)DataGridView_match.Columns[3];
                imageColumn1.ImageLayout = DataGridViewImageCellLayout.Zoom;

                DataGridView_match.Columns[5].DefaultCellStyle.Format = "dd/MM/yyyy";
                DataGridView_match.Columns[6].DefaultCellStyle.Format = @"hh\:mm";

                DataGridView_match.Columns[0].Width = 70;
                DataGridView_match.Columns[1].Width = 40;
                DataGridView_match.Columns[2].Width = 140;
                DataGridView_match.Columns[3].Width = 40;
                DataGridView_match.Columns[4].Width = 140;
                DataGridView_match.Columns[5].Width = 100;
                DataGridView_match.Columns[6].Width = 70;
                DataGridView_match.Columns[7].Width = 90;
                DataGridView_match.Columns[8].Width = 110;


                connection.Close();
            }
        }
        private string GetID(string text)
        {
            string id;

            using (SqlConnection connection = new SqlConnection(@"Data Source=DESKTOP-9HO6E70\SQLEXPRESS;Initial Catalog=SoccerManage;Integrated Security=True"))
            {
                connection.Open();
                string query = "Select IDCLB from CLUB where CLBNAME = '" + text + "'";
                SqlDataAdapter ada = new SqlDataAdapter(query, connection);
                DataTable dt = new DataTable();
                ada.Fill(dt);

                id = dt.Rows[0]["IDCLB"].ToString();

            }

            return id;
        }
        private void button2_Click(object sender, EventArgs e)
        {
            Form formBackground = new Form();

            try
            {
                EditMatch match = new EditMatch(this);

                formBackground.FormBorderStyle = FormBorderStyle.None;
                formBackground.Opacity = .50d;
                formBackground.BackColor = Color.Black;
                formBackground.WindowState = FormWindowState.Maximized;
                formBackground.TopMost = true;
                formBackground.Location = this.Location;
                formBackground.ShowInTaskbar = false;
                formBackground.Show();

                match.Owner = formBackground;

                match.IDREF_cbx.Text = DataGridView_match.CurrentRow.Cells[8].Value.ToString();
                match.tbIDMatch.Text = DataGridView_match.CurrentRow.Cells[0].Value.ToString();
                match.Club_cbx.Text = DataGridView_match.CurrentRow.Cells[2].Value.ToString();
                match.Club_cbx1.Text = DataGridView_match.CurrentRow.Cells[4].Value.ToString();
                match.Stadium_cbx.Text = DataGridView_match.CurrentRow.Cells[7].Value.ToString();
                match.dateTimePicker1.Value = (DateTime)DataGridView_match.CurrentRow.Cells[5].Value + (TimeSpan)DataGridView_match.CurrentRow.Cells[6].Value;
                match.ShowDialog();

                formBackground.Dispose();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            finally
            {
                //formBackground.Dispose();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form formBackground = new Form();

            try
            {
                Match match = new Match(this);

                formBackground.FormBorderStyle = FormBorderStyle.None;
                formBackground.Opacity = .50d;
                formBackground.BackColor = Color.Black;
                formBackground.WindowState = FormWindowState.Maximized;
                //formBackground.TopMost = true;
                formBackground.Location = this.Location;
                formBackground.ShowInTaskbar = false;
                formBackground.Show();

                match.Owner = formBackground;
                match.ShowDialog();

                formBackground.Dispose();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            finally
            {
                formBackground.Dispose();
            }
        }

        private void AddMatch_Load(object sender, EventArgs e)
        {
            LoadMatchs();
        }
    }
}
