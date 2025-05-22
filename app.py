from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <title>Partage de position</title>
</head>
<body>
  <h2>Partager votre position</h2>
  <button onclick="getLocation()">Partager</button>
  <p id="status"></p>

  <script>
    function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(sendPosition);
      } else {
        document.getElementById("status").innerHTML = "Géolocalisation non supportée.";
      }
    }

    function sendPosition(position) {
      fetch("/location", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          lat: position.coords.latitude,
          lon: position.coords.longitude
        })
      }).then(() => {
        document.getElementById("status").innerHTML = "Position envoyée avec succès.";
      });
    }
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/location", methods=["POST"])
def location():
    data = request.get_json()
    print("Position reçue :", data)
    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)