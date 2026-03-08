from django.shortcuts import render

def home(request):
    return render(request, "home.html", {
        "title": "Demo DevSecOps Prueba Numero 3 Snyk",
        "msg": "Django + CI/CD (GitHub Actions + Jenkins) + Sonar/Snyk + Prometheus/Grafana"
    })
