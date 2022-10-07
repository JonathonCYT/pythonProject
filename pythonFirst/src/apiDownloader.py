from fastapi import APIRouter
from starlette.responses import FileResponse
import modelUser
import pdfService

pdf = APIRouter()


@pdf.post('/', response_model=modelUser.userOutput)
async def docCreate(doc: modelUser.userInfo):
    return await pdfService.createDoc(doc)


@pdf.get('/downloader')
async def pdfCreate(pk: int):
    return FileResponse(await pdfService.createPdf(pk))