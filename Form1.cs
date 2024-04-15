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
        private bool isErasing = false;

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

                if (e.KeyCode == Keys.Back)
                    clearPanel();

                if (e.KeyCode == Keys.Up)
                    this.thickness++;

                if (e.KeyCode == Keys.Down)
                    this.thickness--;

                if (e.KeyCode == Keys.E)
                    isErasing = !isErasing;
                

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
            Font thicknessFont = new Font("Arial", 12);
            Brush thicknessBrush = Brushes.Black;
            PointF thicknessPoint = new PointF(10, 10);
            g.FillRectangle(Brushes.GhostWhite, thicknessPoint.X, thicknessPoint.Y, 30, 20);
            g.DrawString(thicknessText, thicknessFont, thicknessBrush, thicknessPoint);

            string commandsText = "E = Erase\nBackSpace = Clear";
            Font commandsFont = new Font("Arial", 12);
            Brush commandsBrush = Brushes.Black;
            PointF commandsPoint = new PointF(10, 30);
            g.FillRectangle(Brushes.GhostWhite, commandsPoint.X, commandsPoint.Y, 200, 40);
            g.DrawString(commandsText, commandsFont, commandsBrush, commandsPoint);
            
        }

        private void clearPanel()
        {
            g.Clear(Color.White);
            pb.Invalidate();
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
                Brush brush = isErasing? Brushes.White : Brushes.Black; 
                var deltaX = e.X - previousPoint.X;
                var deltaY = e.Y - previousPoint.Y;
                var dist = MathF.Sqrt(deltaX * deltaX + deltaY * deltaY);
                for (float d = 0; d < 1; d += 1f / dist)
                {
                    var x = (1 - d) * previousPoint.X + d * e.X;
                    var y = (1 - d) * previousPoint.Y + d * e.Y;
                    g.FillEllipse(brush,
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
