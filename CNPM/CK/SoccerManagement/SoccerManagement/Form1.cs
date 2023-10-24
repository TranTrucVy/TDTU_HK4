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

namespace SoccerManagement
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void LoginButton_Click(object sender, EventArgs e)
        {
            if (UserTextbox1.Text == "admin" && PassTextbox1.Text == "admin")
            {
                Homepage admin = new Homepage();
                this.Close();
                admin.ShowDialog();
            }
            else
            {
                SqlConnection Connection = new SqlConnection(@"Data Source=.;Initial Catalog=QLDB;Integrated Security=True");
                SqlDataAdapter da = new SqlDataAdapter("select * from ACCOUNT where USERNAME = N'" + UserTextbox1.Text + "' and PASS = N'" + PassTextbox1.Text + "'", Connection);
                DataTable dt = new DataTable();
                da.Fill(dt);
                if (dt.Rows.Count > 0)
                {
                    FUser user = new FUser(UserTextbox1.Text);
                    this.Hide();
                    user.Show();
                }
                else MessageBox.Show("Your Username or Password is incorrect \nPlease try again!", "NOTICE", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void guna2Button2_Click(object sender, EventArgs e)
        {
            Signup signup = new Signup();
            this.Hide();
            signup.Show();
        }

        private void ForgotPass_Click(object sender, EventArgs e)
        {
            ForgotPassword forgot = new ForgotPassword();
            this.Hide();
            forgot.Show();
        }

        private void guna2PictureBox1_Click(object sender, EventArgs e)
        {

        }

        private void Form2_TextChanged(object sender, EventArgs e)
        {

        }

        private void UserTextbox_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void Form2_TextChanged_1(object sender, EventArgs e)
        {
            UserTextbox1.Select();
        }
    }
}
