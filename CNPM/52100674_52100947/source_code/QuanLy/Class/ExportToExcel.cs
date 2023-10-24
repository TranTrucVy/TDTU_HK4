using System;
using System.Collections.Generic;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace Quanlysanbong
{
    class ExportToExcel
    {
        public bool ToExcel(DataTable dt, string fileName, string tenex, int p)
        {
            Microsoft.Office.Interop.Excel.Application excel;
            Microsoft.Office.Interop.Excel.Workbook workbook;
            Microsoft.Office.Interop.Excel.Worksheet worksheet;
            Microsoft.Office.Interop.Excel.Range range;

            try
            {
                excel = new Microsoft.Office.Interop.Excel.Application();
                excel.Visible = false;
                excel.DisplayAlerts = false;

                workbook = excel.Workbooks.Add(Type.Missing);

                worksheet = (Microsoft.Office.Interop.Excel.Worksheet)excel.ActiveSheet;

                //Row 1
                //Set Value
                worksheet.Cells[1, "A"] = tenex;
                //Merge Cell
                worksheet.Range[worksheet.Cells[1, "A"], worksheet.Cells[1, p]].Merge();
                worksheet.Range[worksheet.Cells[1, "A"], worksheet.Cells[1, "D"]].Font.Size = 16;
                worksheet.Range[worksheet.Cells[1, "A"], worksheet.Cells[1, "D"]].Cells.HorizontalAlignment = Microsoft.Office.Interop.Excel.XlHAlign.xlHAlignCenter;
                int rowCount = 2;
                foreach (DataRow datarow in dt.Rows)
                {
                    rowCount += 1;
                    for (int i = 1; i <= dt.Columns.Count; i++)
                    {
                        if (rowCount == 3)
                        {
                            excel.Cells[2, i] = dt.Columns[i - 1].ColumnName;
                            excel.Cells.Font.Color = Color.Black;
                        }

                        excel.Cells[rowCount, i] = datarow[i - 1].ToString();

                        if (rowCount > 3)
                        {
                            if (i == dt.Columns.Count)
                            {
                                if (rowCount % 2 == 0)
                                {
                                    range = worksheet.Range[worksheet.Cells[rowCount, 1], worksheet.Cells[rowCount, dt.Columns.Count]];
                                    FormatCell(range, "#bae4c8", Color.Black, false);
                                }
                            }
                        }
                    }
                }

                //resize column
                range = worksheet.Range[worksheet.Cells[1, 1], worksheet.Cells[rowCount, dt.Columns.Count]];
                range.EntireColumn.AutoFit();
                Microsoft.Office.Interop.Excel.Borders border = range.Borders;
                border.LineStyle = Microsoft.Office.Interop.Excel.XlLineStyle.xlContinuous;
                border.Weight = 2d;

                range = worksheet.Range[worksheet.Cells[1, 1], worksheet.Cells[2, dt.Columns.Count]];
                FormatCell(range, "#46b86e", Color.White, true);

                // save workbook
                workbook.SaveAs(fileName);
                workbook.Close();
                excel.Quit();
                return true;
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                return false;
            }
            finally
            {
                workbook = null;
                worksheet = null;
                range = null;
            }
        }

        private void FormatCell(Microsoft.Office.Interop.Excel.Range range, string background, Color color, bool isBool)
        {
            range.Interior.Color = ColorTranslator.FromHtml(background);
            range.Font.Color = ColorTranslator.ToOle(color);
            if (isBool)
            {
                range.Font.Bold = isBool;
            }
        }
    }
}
