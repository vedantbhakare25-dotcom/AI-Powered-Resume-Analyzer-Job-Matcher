def generate_learning_roadmap(role, missing_skills):
    role = role.lower()

    role_base_roadmaps = {
        "backend developer": [
            "Learn REST API fundamentals (HTTP methods, status codes)",
            "Build CRUD APIs using Flask or Node.js",
            "Understand database design and SQL optimization",
            "Implement authentication (JWT, OAuth)",
            "Deploy backend apps on cloud (Render, AWS, or Docker)"
        ],
        "frontend developer": [
            "Master HTML, CSS, and JavaScript fundamentals",
            "Learn React.js and component-based architecture",
            "Understand state management (Redux / Context API)",
            "Optimize UI performance and responsive design",
            "Deploy frontend apps using Vercel or Netlify"
        ],
        "full stack developer": [
            "Build complete MERN or Flask-React projects",
            "Learn API integration between frontend and backend",
            "Understand authentication and session management",
            "Work with SQL and NoSQL databases",
            "Deploy full stack apps with CI/CD pipelines"
        ]
    }

    roadmap = role_base_roadmaps.get(role, [])

    # Add missing-skill focused steps
    skill_specific = {
        "api": "Practice designing and testing RESTful APIs using Postman",
        "docker": "Learn Docker containerization and deployment workflows",
        "aws": "Understand AWS EC2, S3, and cloud deployment basics",
        "react": "Build 3+ projects using React hooks and routing",
        "sql": "Practice complex joins, indexing, and query optimization",
        "python": "Strengthen Python OOP, async programming, and clean architecture"
    }

    for skill in missing_skills:
        if skill.lower() in skill_specific:
            roadmap.append(skill_specific[skill.lower()])

    return roadmap