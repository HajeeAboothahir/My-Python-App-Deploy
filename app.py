
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Hajee Syed Aboothahir | DevOps Engineer</title>

    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: #080d1b;
            color: #ffffff;
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 23px 9%;
            background: #0c1426;
            border-bottom: 1px solid #1e293b;
        }

        .logo {
            font-size: 23px;
            font-weight: 800;
            color: #60a5fa;
        }

        nav a {
            color: #cbd5e1;
            text-decoration: none;
            margin-left: 25px;
            font-size: 14px;
        }

        nav a:hover {
            color: #60a5fa;
        }

        .hero {
            min-height: 570px;
            display: flex;
            align-items: center;
            padding: 100px 9%;
            background:
                radial-gradient(circle at 80% 40%, #17386b 0%, transparent 35%),
                linear-gradient(120deg, #080d1b, #101d35);
        }

        .hero-content {
            max-width: 800px;
        }

        .tag {
            display: inline-block;
            padding: 10px 17px;
            border: 1px solid #2563eb;
            border-radius: 30px;
            color: #60a5fa;
            font-size: 13px;
            margin-bottom: 25px;
        }

        h1 {
            font-size: clamp(38px, 6vw, 65px);
            line-height: 1.15;
            margin-bottom: 22px;
        }

        h1 span {
            color: #60a5fa;
        }

        .hero p {
            color: #a9b8ce;
            font-size: 17px;
            line-height: 1.9;
            max-width: 650px;
            margin-bottom: 30px;
        }

        .btn {
            display: inline-block;
            background: #2563eb;
            color: white;
            text-decoration: none;
            padding: 15px 27px;
            border-radius: 8px;
            font-weight: 600;
            transition: 0.3s;
        }

        .btn:hover {
            background: #3b82f6;
            transform: translateY(-3px);
        }

        section {
            padding: 85px 9%;
        }

        .section-title {
            text-align: center;
            font-size: 35px;
            margin-bottom: 18px;
        }

        .section-subtitle {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 45px;
            line-height: 1.7;
        }

        .about-content {
            max-width: 850px;
            margin: auto;
            text-align: center;
            color: #a9b8ce;
            line-height: 2;
            font-size: 16px;
        }

        .skills {
            background: #0d172a;
        }

        .skill-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
            gap: 18px;
        }

        .skill {
            background: #16243c;
            border: 1px solid #2b4264;
            border-radius: 10px;
            padding: 23px 15px;
            text-align: center;
            transition: 0.3s;
        }

        .skill:hover {
            border-color: #3b82f6;
            transform: translateY(-5px);
        }

        .skill h3 {
            color: #bfdbfe;
            font-size: 16px;
        }

        .projects {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 22px;
        }

        .project {
            background: #111c31;
            border: 1px solid #243550;
            padding: 30px;
            border-radius: 13px;
        }

        .project .icon {
            font-size: 32px;
            margin-bottom: 18px;
        }

        .project h3 {
            margin-bottom: 15px;
            font-size: 19px;
        }

        .project p {
            color: #94a3b8;
            line-height: 1.8;
            font-size: 14px;
        }

        .education {
            background: #0d172a;
            text-align: center;
        }

        .education-box {
            max-width: 700px;
            margin: auto;
            background: #111c31;
            padding: 30px;
            border: 1px solid #243550;
            border-radius: 12px;
            margin-bottom: 18px;
        }

        .education-box h3 {
            color: #60a5fa;
            margin-bottom: 12px;
        }

        .education-box p {
            color: #a9b8ce;
            line-height: 1.8;
        }

        .contact {
            text-align: center;
            background: linear-gradient(120deg, #10254b, #111c31);
            border-radius: 18px;
            padding: 60px 20px;
        }

        .contact p {
            color: #cbd5e1;
            margin: 20px 0 30px;
            line-height: 1.8;
        }

        footer {
            text-align: center;
            padding: 28px;
            color: #64748b;
            border-top: 1px solid #1e293b;
            font-size: 13px;
        }

        @media(max-width: 650px) {
            nav {
                flex-direction: column;
                gap: 20px;
            }

            nav a {
                margin: 0 7px;
            }

            .hero {
                padding: 75px 7%;
            }

            section {
                padding: 65px 7%;
            }

            .section-title {
                font-size: 28px;
            }
        }
    </style>
</head>

<body>

    <nav>
        <div class="logo">Hajee.dev</div>

        <div>
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    <section class="hero" id="home">
        <div class="hero-content">

            <div class="tag">☁ DEVOPS & CLOUD ENGINEER</div>

            <h1>
                Hi, I'm Hajee Syed<br>
                <span>Aboothahir</span>
            </h1>

            <p>
                Passionate about Cloud Computing, DevOps Automation
                and modern infrastructure. I enjoy building, deploying
                and managing applications using AWS, Docker,
                Kubernetes and CI/CD technologies.
            </p>

            <a href="#projects" class="btn">Explore My Projects →</a>

        </div>
    </section>

    <section id="about">

        <h2 class="section-title">About Me</h2>

        <p class="section-subtitle">
            My journey, background and passion for technology.
        </p>

        <div class="about-content">

            I'm Hajee Syed Aboothahir, an aspiring DevOps and Cloud
            Engineer with a background in Mechanical Engineering
            and a Master's degree in International Design Engineering
            from Gdansk University of Technology, Poland.

            <br><br>

            My interest in technology has driven me towards
            software engineering, cloud infrastructure and DevOps.
            I have been developing practical skills through
            technical training, hands-on projects and internship
            experience.

            <br><br>

            I work with technologies such as AWS, Linux, Git,
            Jenkins, Docker, Kubernetes and Terraform. My goal
            is to build reliable infrastructure, automate
            deployments and continuously improve my engineering skills.

            <br><br>

            I believe in continuous learning, practical problem
            solving and growing into a skilled DevOps professional.

        </div>

    </section>

    <section class="skills" id="skills">

        <h2 class="section-title">Technical Skills</h2>

        <p class="section-subtitle">
            Technologies I am learning and working with.
        </p>

        <div class="skill-grid">

            <div class="skill"><h3>☁ AWS Cloud</h3></div>
            <div class="skill"><h3>🐧 Linux</h3></div>
            <div class="skill"><h3>🐳 Docker</h3></div>
            <div class="skill"><h3>☸ Kubernetes</h3></div>
            <div class="skill"><h3>⚙ Jenkins</h3></div>
            <div class="skill"><h3>🔧 Terraform</h3></div>
            <div class="skill"><h3>📦 Git & GitHub</h3></div>
            <div class="skill"><h3>🐍 Python</h3></div>
            <div class="skill"><h3>📊 Prometheus</h3></div>
            <div class="skill"><h3>📈 Grafana</h3></div>
            <div class="skill"><h3>🔄 CI/CD</h3></div>
            <div class="skill"><h3>🤖 Shell Scripting</h3></div>

        </div>

    </section>

    <section id="projects">

        <h2 class="section-title">Hands-on Projects</h2>

        <p class="section-subtitle">
            Practical projects demonstrating my cloud and DevOps learning.
        </p>

        <div class="projects">

            <div class="project">
                <div class="icon">☁️</div>
                <h3>AWS 3-Tier Architecture</h3>
                <p>
                    Designed and worked on a three-tier AWS
                    infrastructure using VPC, public and private
                    subnets, networking and cloud resources.
                </p>
            </div>

            <div class="project">
                <div class="icon">☸️</div>
                <h3>Kubernetes Deployment</h3>
                <p>
                    Hands-on experience deploying containerized
                    applications using Kubernetes, Pods,
                    Services and cluster configurations.
                </p>
            </div>

            <div class="project">
                <div class="icon">🐳</div>
                <h3>Dockerized Flask Application</h3>
                <p>
                    Building a Python Flask web application,
                    creating Docker images and deploying
                    containers on AWS EC2.
                </p>
            </div>

        </div>

    </section>

    <section class="education" id="education">

        <h2 class="section-title">Education</h2>

        <p class="section-subtitle">
            My academic background.
        </p>

        <div class="education-box">
            <h3>M.Sc. International Design Engineering</h3>
            <p>
                Gdansk University of Technology, Poland<br>
                Completed: 2019
            </p>
        </div>

        <div class="education-box">
            <h3>B.Tech Mechanical Engineering</h3>
            <p>
                Dr. M.G.R. Educational and Research Institute, Chennai
            </p>
        </div>

    </section>

    <section id="contact">

        <div class="contact">

            <h2 class="section-title">Let's Connect</h2>

            <p>
                I'm interested in DevOps Engineer,
                Cloud Engineer.
                Let's connect and grow together!
            </p>

            <a href="https://github.com/HajeeAboothahir"
               target="_blank" rel="noopener noreferrer"
               class="btn">
                Visit My GitHub →
            </a>

        </div>

    </section>

    <footer>
        © 2026 Hajee Syed Aboothahir | Built with Python & Flask
    </footer>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
