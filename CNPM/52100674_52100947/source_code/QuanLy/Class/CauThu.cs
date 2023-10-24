using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuanLy.Class
{
    internal class CauThu
    {
        ketnoi kn = new ketnoi();
        public DataTable DanhSach()
        {
            string sql = "select CauThu.Id[Mã cầu thủ],HoTen[Họ và tên],QueQuan[Quê quán],NamSinh[Năm sinh],SoAo[Số áo],TenCLB[Câu lạc bộ] from CauThu inner join CauLacBo on CauThu.IdCLB=CauLacBo.Id";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public DataTable DanhSach(string key)
        {
            string sql = "select CauThu.Id[Mã cầu thủ],HoTen[Họ và tên],QueQuan[Quê quán],NamSinh[Năm sinh],SoAo[Số áo],TenCLB[Câu lạc bộ] from CauThu inner join CauLacBo on CauThu.IdCLB=CauLacBo.Id where TenCLB like N'%" + key + "%' or HoTen like N'%" + key + "%'";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public DataTable CLB(int key)
        {
            string sql = "select CauThu.Id[Mã cầu thủ],HoTen[Họ và tên],QueQuan[Quê quán],NamSinh[Năm sinh],SoAo[Số áo],TenCLB[Câu lạc bộ] from CauThu inner join CauLacBo on CauThu.IdCLB=CauLacBo.Id where CauLacBo.Id=" + key + "";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public void ThemCT(string ht,string qq, int ns, int soao,int maclb)
        {
            string sql = "insert into CauThu values (N'" + ht + "',N'" + qq + "','" + ns + "','"+soao+"','"+maclb+"')";
            kn.hamxuly(sql);
        }
        public void SuaCT(int malt, string ht, string qq, int ns, int soao, int maclb)
        {
            string sql = "update CauThu set HoTen=N'" + ht + "',QueQuan=N'" + qq + "',NamSinh='" + ns+ "',SoAo='"+soao+"',IdCLB='"+maclb+"' where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
        public void XoaCT(int malt)
        {
            string sql = "delete from CauThu  where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
    }
}
