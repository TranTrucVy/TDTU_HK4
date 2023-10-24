using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace QuanLy.Class
{
    internal class MuaGiai
    {
        ketnoi kn = new ketnoi();
        public DataTable DanhSach()
        {
            string sql = "select Id[Mã mùa giải],TenMuaGiai[Tên mùa giải] from MuaGiai";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public DataTable DanhSach(string key)
        {
            string sql = "select Id[Mã mùa giải],TenMuaGiai[Tên mùa giải] from MuaGiai where TenMuaGiai like N'%" + key + "%'";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public void ThemMG(string ten)
        {
            string sql = "insert into MuaGiai values (N'" + ten + "')";
            kn.hamxuly(sql);
        }
        public void SuaMG(int malt, string lt)
        {
            string sql = "update MuaGiai set TenMuaGiai=N'" + lt + "' where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
        public void XoaMG(int malt)
        {
            string sql = "delete from MuaGiai  where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
    }
}
