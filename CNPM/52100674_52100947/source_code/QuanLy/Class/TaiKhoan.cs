using QuanLy;
using System.Data.SqlClient;

namespace QuanLy.Class
{
    internal class TaiKhoan
    {
        ketnoi kn = new ketnoi();
        public void DangKi(string tdn, string mk,string sdt,string email)
        {
            string sql = "insert into TaiKhoan values ('" + tdn + "','" + mk + "',2,'"+sdt+"','"+email+"')";
            kn.hamxuly(sql);
        }
        public int DangNhap(string tdn, string mk)
        {
            SqlConnection con = kn.GetConnection();
            con.Open();
            string sql1 = "select IdPQ from TaiKhoan where TenDangNhap='" + tdn + "' and MatKhau='" + mk + "'";
            SqlCommand cmd1 = new SqlCommand(sql1, con);
            SqlDataReader rd1 = cmd1.ExecuteReader();
            if (rd1.Read() == false)
            {
                return -1;
            }

            else
            {
                return int.Parse(rd1[0].ToString());
            }
        }
        public int CheckTK(string tdn)
        {
            SqlConnection con = kn.GetConnection();
            con.Open();
            string sql1 = "select * from TaiKhoan where TenDangNhap like '%" + tdn + "%'";
            SqlCommand cmd1 = new SqlCommand(sql1, con);
            SqlDataReader rd1 = cmd1.ExecuteReader();
            if (rd1.Read() == false)
            {
                return -1;
            }

            else
            {
                return 1;
            }
        }

    }
}
