using System.Drawing;
using System.Windows.Forms;
using System;
using Timer = System.Windows.Forms.Timer;

namespace HandWriteRecognize
{
    public partial class Form1 : Form
    {
        PictureBox pb = new PictureBox();
        Bitmap bmp;
        Timer tm;
        Graphics g;
        private bool isDrawing = false;
        private Point previousPoint;
        private int thickness = 5;

        public Form1()
        {
            InitializeComponent();

            this.tm = new Timer();
            this.tm.Interval = 20;

            this.BackColor = Color.White;

            this.WindowState = FormWindowState.Maximized;
            this.FormBorderStyle = FormBorderStyle.None;
            
            this.Controls.Add(pb);
            pb.Dock = DockStyle.Fill;

            pb.MouseDown += pb_MouseDown;
            pb.MouseMove += pb_MouseMove;
            pb.MouseUp += pb_MouseUp;

            this.KeyDown += (o, e) =>
            {
                if (e.KeyCode == Keys.Escape)
                    Application.Exit();

                if (e.KeyCode == Keys.Up)
                    this.thickness++;

                if (e.KeyCode == Keys.Down)
                    this.thickness--;


            };

            this.Load += (o, e) =>
            {
                this.bmp = new Bitmap(pb.Width, pb.Height);
                g = Graphics.FromImage(bmp);
                g.Clear(Color.White);
                this.pb.Image = bmp;
            };

            tm.Tick += (o, e) =>
            {
                Frame();
                pb.Refresh();
            };
            tm.Start();
        }

        void Frame()
        {
            string thicknessText = $"{thickness}";
            Font font = new Font("Arial", 12);
            Brush brush = Brushes.Black;
            PointF point = new PointF(10, 10);
            g.FillRectangle(Brushes.GhostWhite, point.X, point.Y, 30, 20);
            g.DrawString(thicknessText, font, brush, point);
        }

        private void pb_MouseDown(object sender, MouseEventArgs e)
        {
            isDrawing = true;
            previousPoint = e.Location;
        }

        private void pb_MouseUp(object sender, MouseEventArgs e)
        {
            isDrawing = false;
        }
        private void pb_MouseMove(object sender, MouseEventArgs e)
        {
            if (isDrawing)
            {
                var deltaX = e.X - previousPoint.X;
                var deltaY = e.Y - previousPoint.Y;
                var dist = MathF.Sqrt(deltaX * deltaX + deltaY * deltaY);
                for (float d = 0; d < 1; d += 1f / dist)
                {
                    var x = (1 - d) * previousPoint.X + d * e.X;
                    var y = (1 - d) * previousPoint.Y + d * e.Y;
                    g.FillEllipse(Brushes.Black, 
                        x - thickness / 2, 
                        y - thickness / 2,
                        thickness, thickness
                    );
                }
                previousPoint = e.Location;
                pb.Invalidate();
            }
        }
    }

}
