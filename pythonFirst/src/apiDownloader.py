from fastapi import APIRouter
from starlette.responses import FileResponse
import modelUsers
import pdfService

pdf = APIRouter()


@pdf.post('/', response_model=modelUsers.userOutput)
async def docCreate(doc: modelUsers.userInfo):
    return await pdfService.createDoc(doc)


@pdf.get('/downloader')
async def pdfCreate(pk: int):
    return FileResponse(await pdfService.createPdf(pk))