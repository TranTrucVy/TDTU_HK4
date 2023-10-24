using System.Data;

namespace QuanLy.Class
{
    internal class LichThiDau
    {
        ketnoi kn = new ketnoi();
        public DataTable DanhSach()
        {
            string sql = "select LichThiDau.Id[Mã lịch thi đấu],CauLacBo.TenCLB[Câu lạc bộ 1],c.TenCLB[Câu lạc bộ 2],TenSVD[Sân vận động],TenMuaGiai[Mùa giải],GioThiDau[Giờ thi đấu],NgayThiDau[Ngày thi đấu] from LichThiDau inner join CauLacBo on CauLacBo.Id=LichThiDau.IdCLB1 inner join CauLacBo c on c.Id=LichThiDau.IdCLB2 inner join SanVD on SanVD.Id=LichThiDau.IdSVD inner join MuaGiai on MuaGiai.Id=LichThiDau.IdMuaGiai";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public DataTable DanhSach(int mg)
        {
            string sql = "select LichThiDau.Id[Mã lịch thi đấu],CauLacBo.TenCLB[Câu lạc bộ 1],c.TenCLB[Câu lạc bộ 2],TenSVD[Sân vận động],TenMuaGiai[Mùa giải],GioThiDau[Giờ thi đấu],NgayThiDau[Ngày thi đấu] from LichThiDau inner join CauLacBo on CauLacBo.Id=LichThiDau.IdCLB1 inner join CauLacBo c on c.Id=LichThiDau.IdCLB2 inner join SanVD on SanVD.Id=LichThiDau.IdSVD inner join MuaGiai on MuaGiai.Id=LichThiDau.IdMuaGiai where MuaGiai.Id='" + mg+"'";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public DataTable LTD(int mg)
        {
            string sql = "select LichThiDau.Id[Mã lịch thi đấu],CauLacBo.TenCLB[Câu lạc bộ 1],c.TenCLB[Câu lạc bộ 2],TenSVD[Sân vận động],TenMuaGiai[Mùa giải],GioThiDau[Giờ thi đấu],NgayThiDau[Ngày thi đấu] from LichThiDau inner join CauLacBo on CauLacBo.Id=LichThiDau.IdCLB1 inner join CauLacBo c on c.Id=LichThiDau.IdCLB2 inner join SanVD on SanVD.Id=LichThiDau.IdSVD inner join MuaGiai on MuaGiai.Id=LichThiDau.IdMuaGiai where MuaGiai.Id='" + mg + "' order by NgayThiDau asc";
            DataTable dt = kn.GetTable(sql);
            return dt;
        }
        public void ThemLTD(int clb1, int clb2, string date, int svd, int mg,string gtd)
        {
            string sql = "insert into LichThiDau values ('" + clb1 + "','" + clb2 + "','" + date + "',N'" + svd + "','" + mg + "','"+gtd+"')";
            kn.hamxuly(sql);
        }
        public void SuaLTD(int malt, int clb1, int clb2, string date, int svd, int mg,string gtd)
        {
            string sql = "update LichThiDau set IdCLB1='" + clb1 + "',IdCLB2='" + clb2 + "',NgayThiDau='" + date + "',IdSVD='" + svd + "',IdMuaGiai='" + mg + "',GioThiDau='"+gtd+"' where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
        public void XoaLTD(int malt)
        {
            string sql = "delete from LichThiDau  where Id='" + malt + "'";
            kn.hamxuly(sql);
        }
    }
}
