using System;
using System.Windows.Forms;
using Python.Runtime;

Runtime.PythonDLL = "python311.dll";
PythonEngine.Initialize();

dynamic tf = Py.Import("tensorflow");
dynamic np = Py.Import("numpy");

dynamic model = tf.keras.models.load_model("checkpoints/crop-91-85.keras");

// pip install pillow
dynamic list = new PyList();
list.append(tf.keras.utils.load_img("imgTest/f3.png"));
list.append(tf.keras.utils.load_img("imgTest/f3.png"));
dynamic data = np.array(list);

MessageBox.Show("Chegou");

// dynamic result = model.predict(data);
// MessageBox.Show((np.argmax(result) + 1).ToString());

try
{
    dynamic result = model.predict(data);
    MessageBox.Show((np.argmax(result) + 1).ToString());
}
catch (Exception ex)
{
    MessageBox.Show("An error occurred: " + ex.Message);
}


PythonEngine.Shutdown();