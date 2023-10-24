using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SoccerManagement
{
    public partial class FUser : Form
    {
        private string username;
        public FUser()
        {
            Control.CheckForIllegalCrossThreadCalls = false;
            InitializeComponent();
        }
        public FUser(string u)
        {
            InitializeComponent();
            this.username = u;

        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}
