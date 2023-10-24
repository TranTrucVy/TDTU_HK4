using System;
using System.Collections.Generic;
using System.Data;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuanLy.Class
{
    internal class XepHang
    {
        ketnoi kn = new ketnoi();
        public DataTable DanhSach(int mg)
        {
            string sql = "select Row_number() over(order by Diem desc) [Xếp hạng],TenCLB[Câu lạc bộ],Diem[Điểm],TenMuaGiai[Mùa giải] from XepHang inner join CauLacBo c on XepHang.IdCLB=c.Id inner join MuaGiai on MuaGiai.Id=XepHang.IdMuaGiai where IdMuaGiai = " + mg+ " order by Diem desc";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public int kiemtra(int mg,int doi)
        {
            SqlConnection con = kn.GetConnection();
            con.Open();
            string sql1 = "select * from XepHang where IdMuaGiai='" + mg + "' and IdCLB='" + doi + "'";
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
        public void ThemXH(int mg, int clb,int diem)
        {
            string sql = "insert into XepHang values ('" + mg + "','" + clb + "',N'" + diem + "')";
            kn.hamxuly(sql);
        }
        public void SuaXH(int mg, int clb, int diem)
        {
            string sql = "update XepHang set Diem=Diem+" + diem + " where IdMuaGiai=" + mg + " and IdCLB="+clb+"";
            kn.hamxuly(sql);
        }
    }
}
