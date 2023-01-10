from fastapi import APIRouter
from schema.metric import Metric


router = APIRouter()

#POST
@router.post("/metric")
async def create(metric: Metric):
    return metric.save()
#GET
@router.get("/metrics")
async def all():
    return Metric.all_pks()
#PUT
@router.put("/metric/{pk}")
async def update(pk:str,metric:Metric):
    _metric = Metric.get(pk)
    _metric.newton = metric.newton
    _metric.date = metric.date
    return _metric.save()
#DELETE
@router.delete("/metric/{pk}")
async def delete(pk: str):
    _metric = Metric.get(pk)
    return _metric.delete(pk)

