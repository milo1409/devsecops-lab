from django.shortcuts import render

def home(request):
    return render(request, "home.html", {
        "title": "Demo DevSecOps",
        "msg": "Django + CI/CD (GitHub Actions + Jenkins) + Sonar/Snyk + Prometheus/Grafana"
    })
