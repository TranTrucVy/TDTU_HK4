using QuanLy;
using System.Data;

namespace QuanLy.Class
{
    internal class SanVD
    {
        ketnoi kn = new ketnoi();
        public DataTable DanhSach()
        {
            string sql = "select Id[Mã],TenSVD[Tên sân vận động],SucChua[Sức chứa],ThanhPho[Thành phố] from SanVD";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public DataTable DanhSach(string key)
        {
            string sql = "select Id[Mã],TenSVD[Tên sân vận động],SucChua[Sức chứa],ThanhPho[Thành phố] from SanVD where TenSVD like N'%" + key + "%'  or ThanhPho like N'%" + key + "%'";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public void ThemSVD(string lt, string sc, string tp)
        {
            string sql = "insert into SanVD(TenSVD,SucChua,ThanhPho) values (N'" + lt + "','" + sc + "',N'" + tp + "')";
            kn.hamxuly(sql);
        }
        public void SuaSVD(int malt, string lt, string sc, string tp)
        {
            string sql = "update SanVD set TenSVD=N'" + lt + "',SucChua='" + sc + "',ThanhPho=N'" + tp + "' where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
        public void XoaSVD(int malt)
        {
            string sql = "delete from SanVD  where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
    }
}
