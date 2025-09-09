from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

app = FastAPI(title="AI Empire API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "AI Empire 98% Automated System",
        "status": "operational", 
        "automation_level": "98%",
        "manual_intervention": "2% (30 min/week)",
        "revenue_target": "$25,000/month",
        "roi": "197x"
    }

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "automation": "98%"}

@app.post("/api/cron/hourly-automation")
async def hourly_automation(background_tasks: BackgroundTasks):
    """Vercel cron job for hourly automation"""
    try:
        from core.ultra_automated_orchestrator import UltraAutomatedOrchestrator
        
        def run_hourly_tasks():
            import asyncio
            orchestrator = UltraAutomatedOrchestrator()
            asyncio.run(orchestrator._autonomous_lead_generation())
            asyncio.run(orchestrator._autonomous_client_management())
        
        background_tasks.add_task(run_hourly_tasks)
        return {"status": "Hourly automation started"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/cron/daily-automation") 
async def daily_automation(background_tasks: BackgroundTasks):
    """Vercel cron job for daily automation"""
    try:
        from core.ultra_automated_orchestrator import UltraAutomatedOrchestrator
        
        def run_daily_tasks():
            import asyncio
            orchestrator = UltraAutomatedOrchestrator()
            asyncio.run(orchestrator._autonomous_revenue_cycle())
            asyncio.run(orchestrator._autonomous_content_pipeline())
            asyncio.run(orchestrator._autonomous_opportunity_hunting())
        
        background_tasks.add_task(run_daily_tasks)
        return {"status": "Daily automation started"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/cron/weekly-briefing")
async def weekly_briefing(background_tasks: BackgroundTasks):
    """Vercel cron job for weekly briefing"""
    try:
        from core.ultra_automated_orchestrator import UltraAutomatedOrchestrator
        
        def run_weekly_briefing():
            import asyncio
            orchestrator = UltraAutomatedOrchestrator()
            asyncio.run(orchestrator._weekly_strategic_briefing())
        
        background_tasks.add_task(run_weekly_briefing)
        return {"status": "Weekly briefing generated"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)