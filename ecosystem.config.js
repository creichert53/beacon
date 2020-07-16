module.exports = {
  apps: [{
    name: "frontend",
    script: "npm",
    args: "start",
    watch: ["src"],
    env: {
      NODE_ENV: "development",
    },
    env_production: {
      NODE_ENV: "production",
    }
  },{
    name: "server",
    script: "bacnet/index.py",
    interpreter: "python3",
    watch: ["bacnet"],
    env: {
      NODE_ENV: "development",
    },
    env_production: {
      NODE_ENV: "production",
    }
  }]
}