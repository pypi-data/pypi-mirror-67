#!/usr/bin/env python3
# coding: utf-8
import json
from typing import cast

from flask import Blueprint, Response, request
from flask.json import jsonify

from genpei.const import GET_STATUS_CODE, POST_STATUS_CODE
from genpei.run import (cancel_run, fork_run, get_run_log, prepare_exe_dir,
                        validate_run_id, validate_run_request,
                        validate_wf_type)
from genpei.type import (RunId, RunListResponse, RunLog, RunRequest, RunStatus,
                         ServiceInfo, State)
from genpei.util import (generate_run_id, get_all_run_ids, get_state,
                         read_service_info, write_file)

app_bp = Blueprint("genpei", __name__)


@app_bp.route("/service-info", methods=["GET"])
def get_service_info() -> Response:
    """
    May include information related (but not limited to) the workflow
    descriptor formats, versions supported, the WES API versions supported,
    and information about general service availability.
    """
    res_body: ServiceInfo = read_service_info()
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/runs", methods=["GET"])
def get_runs() -> Response:
    """
    This list should be provided in a stable ordering. (The actual ordering is
    implementation dependent.) When paging through the list, the client should
    not make assumptions about live updates, but should assume the contents of
    the list reflect the workflow list at the moment that the first page is
    requested. To monitor a specific workflow run, use GetRunStatus or
    GetRunLog.
    """
    res_body: RunListResponse = {
        "runs": [],
        "next_page_token": ""
    }
    for run_id in get_all_run_ids():
        res_body["runs"].append({
            "run_id": run_id,
            "state": get_state(run_id).name  # type: ignore
        })
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/runs", methods=["POST"])
def post_runs() -> Response:
    """
    This endpoint creates a new workflow run and returns a `RunId` to monitor
    its progress.
    """
    run_request: RunRequest = cast(RunRequest, dict(request.form))
    validate_run_request(run_request)
    validate_wf_type(run_request["workflow_type"],
                     run_request["workflow_type_version"])
    run_id: str = generate_run_id()
    write_file(run_id, "run_request", json.dumps(run_request, indent=2))
    write_file(run_id, "wf_params", run_request["workflow_params"])
    prepare_exe_dir(run_id, request.files)
    write_file(run_id, "state", State.QUEUED.name)
    fork_run(run_id, run_request)
    response: Response = jsonify({
        "run_id": run_id
    })
    response.status_code = POST_STATUS_CODE

    return response


@app_bp.route("/runs/<run_id>", methods=["GET"])
def get_runs_id(run_id: str) -> Response:
    """
    This endpoint provides detailed information about a given workflow run.
    The returned result has information about the outputs produced by this
    workflow (if available), a log object which allows the stderr and stdout
    to be retrieved, a log array so stderr/stdout for individual tasks can be
    retrieved, and the overall state of the workflow run (e.g. RUNNING, see
    the State section).
    """
    validate_run_id(run_id)
    res_body: RunLog = get_run_log(run_id)
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response


@app_bp.route("/runs/<run_id>/cancel", methods=["POST"])
def post_runs_id_cancel(run_id: str) -> Response:
    """
    Cancel a running workflow.
    """
    validate_run_id(run_id)
    cancel_run(run_id)
    res_body: RunId = {"run_id": run_id}
    response: Response = jsonify(res_body)
    response.status_code = POST_STATUS_CODE

    return response


@app_bp.route("/runs/<run_id>/status", methods=["GET"])
def get_runs_id_status(run_id: str) -> Response:
    """
    This provides an abbreviated (and likely fast depending on implementation)
    status of the running workflow, returning a simple result with the overall
    state of the workflow run (e.g. RUNNING, see the State section).
    """
    validate_run_id(run_id)
    res_body: RunStatus = {
        "run_id": run_id,
        "state": get_state(run_id).name  # type: ignore
    }
    response: Response = jsonify(res_body)
    response.status_code = GET_STATUS_CODE

    return response
