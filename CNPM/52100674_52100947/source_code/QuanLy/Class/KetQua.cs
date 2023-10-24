using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuanLy.Class
{
    internal class KetQua
    {
        ketnoi kn = new ketnoi();
        //public DataTable DanhSach()
        //{
        //    string sql = "select CauLacBo.Id[Mã],TenCLB[Tên câu lạc bộ],SanVD.[TenSVD][Tên sân vận động],HuanLuyenVien[Huấn luyện viên] from CauLacBo inner join SanVD on SanVD.Id=CauLacBo.IdSVD";
        //    DataTable dt = kn.GetTable(sql);
        //    return dt;
        //}
        //public DataTable DanhSach(string key)
        //{
        //    string sql = "select CauLacBo.Id[Mã],TenCLB[Tên câu lạc bộ],SanVD.[TenSVD][Tên sân vận động],HuanLuyenVien[Huấn luyện viên] from CauLacBo inner join SanVD on SanVD.Id=CauLacBo.IdSVD where TenCLB like N'%" + key + "%'";
        //    DataTable dt = kn.GetTable(sql);
        //    return dt;
        //}
        public void ThemKQ(int maltd, int d1, int d2)
        {
            string sql = "insert into KetQua values ('" + maltd + "','" + d1 + "','" + d2 + "')";
            kn.hamxuly(sql);
        }
        public void SuaCLB(int malt, string lt, int sc, string tp)
        {
            string sql = "update CauLacBo set TenCLB=N'" + lt + "',IdSVD='" + sc + "',HuanLuyenVien=N'" + tp + "' where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
        public void XoaCLB(int malt)
        {
            string sql = "delete from CauLacBo  where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
    }
}
