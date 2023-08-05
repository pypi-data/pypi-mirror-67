#ifndef N_FLATS
    #error "Please provide the N_FLATS variable"
#endif

#ifndef N_DARKS
    #error "Please provide the N_FLATS variable"
#endif



/**
 * In-place flat-field normalization.
 * This kernel assumes that all the radios are loaded into memory
 * (although not necessarily the full radios images)
 * and in radios[x, y z], z in the radio index
 *
 * radios: 3D array
 * flats: 3D array
 * darks: 3D array
 * Nx: number of pixel horizontally in the radios
 * Nx: number of pixel vertically in the radios
 * Nx: number of radios
 * flats_indices: indices of flats, in sorted order
 * darks_indices: indices of darks, in sorted order
 **/
__global__ void flatfield_normalization(
    float* radios,
    float* flats,
    float* darks,
    int Nx,
    int Ny,
    int Nz,
    int* flats_indices,
    int* darks_indices,
    int* radios_indices
) {
    uint x = blockDim.x * blockIdx.x + threadIdx.x;
    uint y = blockDim.y * blockIdx.y + threadIdx.y;
    uint z = blockDim.z * blockIdx.z + threadIdx.z;
    if ((x >= Nx) || (y >= Ny) || (z >= Nz)) return;
    uint pos = (z*Ny+y)*Nx + x;
    int radio_idx = radios_indices[z];

    float dark_val = 0.0f, flat_val = 1.0f;

    #if N_FLATS == 1
        flat_val = flats[y*Nx + x];
    #else
        // interpolation between 2 flats
        for (int i = 0; i < N_FLATS-1; i++) {
            int ind_prev = flats_indices[i];
            int ind_next = flats_indices[i+1];
            if (ind_prev >= radio_idx) {
                flat_val = flats[(i*Ny+y)*Nx + x];
                break;
            }
            else if (ind_prev < radio_idx && radio_idx < ind_next) {
                // Linear interpolation
                // TODO nearest interpolation
                int delta = ind_next - ind_prev;
                float w1 = 1.0f - (radio_idx*1.0f - ind_prev) / delta;
                float w2 = 1.0f - (ind_next*1.0f - radio_idx) / delta;
                flat_val = w1 * flats[(i*Ny+y)*Nx + x] + w2 * flats[((i+1)*Ny+y)*Nx + x];
                break;
            }
            else if (ind_next <= radio_idx) {
                flat_val = flats[((i+1)*Ny+y)*Nx + x];
                break;
            }
        }
    #endif
    #if (N_DARKS == 1)
        dark_val = darks[y*Nx + x];
    #else
        // TODO interpolate between darks
        // Same as above...
        #error "N_DARKS > 1 is not supported yet"
    #endif

    radios[pos] = (radios[pos] - dark_val) / (flat_val - dark_val);
}
