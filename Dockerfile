FROM python:3
RUN pip install newsbeuter-spread
CMD [ "python", "-m", "newsbeuter_spread.app"]
